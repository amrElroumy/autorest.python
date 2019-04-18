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

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration import AutoRestHeadExceptionTestServiceConfiguration
from .operations import HeadExceptionOperations


class AutoRestHeadExceptionTestService(PipelineClient):
    """Test Infrastructure for AutoRest


    :ivar head_exception: HeadException operations
    :vartype head_exception: headexceptions.operations.HeadExceptionOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None, config=None, **kwargs):

        self._config = config or AutoRestHeadExceptionTestServiceConfiguration(credentials, **kwargs)
        super(AutoRestHeadExceptionTestService, self).__init__(base_url=base_url, config=self._config, **kwargs)

        client_models = {}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.head_exception = HeadExceptionOperations(
            self, self._config, self._serialize, self._deserialize)
