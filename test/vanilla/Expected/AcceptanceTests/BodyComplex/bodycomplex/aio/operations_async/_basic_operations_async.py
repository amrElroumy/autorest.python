# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from ... import models


class BasicOperations:
    """BasicOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: API ID. Constant value: "2016-02-29".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config
        self.api_version = "2016-02-29"

    async def get_valid(self, *, cls=None, **kwargs):
        """Get complex type {id: 2, name: 'abc', color: 'YELLOW'}.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Basic', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_valid.metadata = {'url': '/complex/basic/valid'}

    async def put_valid(self, complex_body, *, cls=None, **kwargs):
        """Please put {id: 2, name: 'abc', color: 'Magenta'}.

        :param complex_body: Please put {id: 2, name: 'abc', color: 'Magenta'}
        :type complex_body: ~bodycomplex.models.Basic
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Basic')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_valid.metadata = {'url': '/complex/basic/valid'}

    async def get_invalid(self, *, cls=None, **kwargs):
        """Get a basic complex type that is invalid for the local strong type.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Basic', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_invalid.metadata = {'url': '/complex/basic/invalid'}

    async def get_empty(self, *, cls=None, **kwargs):
        """Get a basic complex type that is empty.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Basic', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_empty.metadata = {'url': '/complex/basic/empty'}

    async def get_null(self, *, cls=None, **kwargs):
        """Get a basic complex type whose properties are null.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Basic', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_null.metadata = {'url': '/complex/basic/null'}

    async def get_not_provided(self, *, cls=None, **kwargs):
        """Get a basic complex type while the server doesn't provide a response
        payload.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: Basic or the result of cls(response)
        :rtype: ~bodycomplex.models.Basic
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_not_provided.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Basic', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_not_provided.metadata = {'url': '/complex/basic/notprovided'}
