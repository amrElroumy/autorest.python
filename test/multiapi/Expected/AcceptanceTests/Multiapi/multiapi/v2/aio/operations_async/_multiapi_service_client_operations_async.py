# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TYPE_CHECKING, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core import AsyncPipelineClient
    from msrest import Deserializer, Serializer

    from .._configuration_async import MultiapiServiceClientConfiguration

    class AbstractServiceClient(object):
        """Abstract class of a service client to help with type hints for the following mixin class"""

        def __init__(self):
            # type: () -> None
            """
            Init for abstract service client class
            """

        @property
        def _client(self):
            # type: () -> AsyncPipelineClient
            """Pipeline client
            :rtype: AsyncPipelineClient
            """

        @_client.setter
        def _client(self, value):
            # type: (AsyncPipelineClient) -> None
            """Set the pipeline client"""

        @property
        def _config(self):
            # type: () -> MultiapiServiceClientConfiguration
            """Configuration of service client
            :rtype: MultiapiServiceClientConfiguration
            """

        @_config.setter
        def _config(self, value):
            # type: (MultiapiServiceClientConfiguration) -> None
            """Set the configuration"""

        @property
        def _serialize(self):
            # type: () -> Serializer
            """Serializer
            :rtype: Serializer
            """

        @_serialize.setter
        def _serialize(self, value):
            # type: (Serializer) -> None
            """Set the serializer"""

        @property
        def _deserialize(self):
            # type: () -> Deserializer
            """Deserializer
            :rtype: Deserializer
            """

        @_deserialize.setter
        def _deserialize(self, value):
            # type: (Deserializer) -> None
            """Set the deserializer"""

    # https://github.com/python/mypy/issues/5837
    _MIXIN_BASE = AbstractServiceClient
else:
    _MIXIN_BASE = object

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MultiapiServiceClientOperationsMixin(_MIXIN_BASE):

    async def test_one(
        self,
        id: int,
        message: Optional[str] = None,
        **kwargs
    ) -> "models.ModelTwo":
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo, or the result of cls(response)
        :rtype: ~multiapi.v2.models.ModelTwo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ModelTwo"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2.0.0"

        # Construct URL
        url = self.test_one.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['id'] = self._serialize.query("id", id, 'int')
        if message is not None:
            query_parameters['message'] = self._serialize.query("message", message, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ModelTwo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    test_one.metadata = {'url': '/multiapi/testOneEndpoint'}  # type: ignore
