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


from .. import models


class BoolModelOperations(object):
    """BoolModelOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    def get_true(self, cls=None, **kwargs):
        """Get true Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        # Construct URL
        url = self.get_true.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_true.metadata = {'url': '/bool/true'}

    def put_true(self, cls=None, **kwargs):
        """Set Boolean value true.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        bool_body = True

        # Construct URL
        url = self.put_true.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_true.metadata = {'url': '/bool/true'}

    def get_false(self, cls=None, **kwargs):
        """Get false Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        # Construct URL
        url = self.get_false.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_false.metadata = {'url': '/bool/false'}

    def put_false(self, cls=None, **kwargs):
        """Set Boolean value false.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        bool_body = False

        # Construct URL
        url = self.put_false.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_false.metadata = {'url': '/bool/false'}

    def get_null(self, cls=None, **kwargs):
        """Get null Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_null.metadata = {'url': '/bool/null'}

    def get_invalid(self, cls=None, **kwargs):
        """Get invalid Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_invalid.metadata = {'url': '/bool/invalid'}
