# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Set

from .base_model import BaseModel
from .operation import Operation
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .imports import FileImport, ImportType, TypingSection


_LOGGER = logging.getLogger(__name__)


class OperationGroup(BaseModel):
    """Represent an operation group.

    """
    def __init__(
        self,
        code_model,
        yaml_data: Dict[str, Any],
        name: str,
        class_name: str,
        operations: List[Operation],
        api_versions: Set[str]
    ) -> None:
        super().__init__(yaml_data)
        self.code_model = code_model
        self.name = name
        self.class_name = class_name
        self.operations = operations
        self.api_versions = api_versions

    def _add_imports_for_abstract_service_client(self, async_mode: bool):
        file_import = FileImport()
        if self.code_model.options["azure_arm"]:
            file_import.add_from_import(
                "azure.mgmt.core",
                self.code_model.service_client.pipeline_class(self.code_model, async_mode),
                ImportType.AZURECORE,
                TypingSection.TYPING
            )
        else:
            file_import.add_from_import(
                "azure.core",
                self.code_model.service_client.pipeline_class(self.code_model, async_mode),
                ImportType.AZURECORE,
                TypingSection.TYPING
            )

        file_import.add_from_import("msrest", "Serializer", ImportType.AZURECORE, TypingSection.TYPING)
        file_import.add_from_import("msrest", "Deserializer", ImportType.AZURECORE, TypingSection.TYPING)
        if async_mode:
            file_import.add_from_import(
                ".._configuration_async",
                f"{ self.code_model.class_name }Configuration",
                ImportType.LOCAL,
                TypingSection.TYPING
            )
        else:
            file_import.add_from_import(
                ".._configuration",
                f"{ self.code_model.class_name }Configuration",
                ImportType.LOCAL,
                TypingSection.TYPING
            )
        return file_import

    def imports(self, async_mode: bool, has_schemas: bool) -> FileImport:
        file_import = FileImport()
        file_import.add_from_import("azure.core.exceptions", "ResourceNotFoundError", ImportType.AZURECORE)
        file_import.add_from_import("azure.core.exceptions", "ResourceExistsError", ImportType.AZURECORE)
        for operation in self.operations:
            file_import.merge(operation.imports(self.code_model, async_mode))
        if self.code_model.options["tracing"]:
            if async_mode:
                file_import.add_from_import(
                    "azure.core.tracing.decorator_async", "distributed_trace_async", ImportType.AZURECORE,
                )
            else:
                file_import.add_from_import(
                    "azure.core.tracing.decorator", "distributed_trace", ImportType.AZURECORE,
                )
        if has_schemas:
            if async_mode:
                file_import.add_from_import("...", "models", ImportType.LOCAL)
            else:
                file_import.add_from_import("..", "models", ImportType.LOCAL)

        if self.is_empty_operation_group:
            # adding imports for abstract class for typing in mixin operation groups
            file_import.merge(self._add_imports_for_abstract_service_client(async_mode))
        return file_import

    def get_filename(self, async_mode: bool) -> str:
        basename = self.name
        if self.is_empty_operation_group:
            basename = self.code_model.module_name
        async_suffix = "_async" if async_mode else ""

        if basename == "operations":
            return f"_operations{async_suffix}"
        return f"_{basename}_operations{async_suffix}"

    @property
    def is_empty_operation_group(self) -> bool:
        """The operation group with no name is the direct client methods.
        """
        return not self.yaml_data["language"]["default"]["name"]

    @classmethod
    def from_yaml(cls, code_model, yaml_data: Dict[str, Any]) -> "OperationGroup":
        name = yaml_data["language"]["python"]["name"]
        _LOGGER.debug("Parsing %s operation group", name)

        operations = []
        api_versions: Set[str] = set()
        for operation_yaml in yaml_data["operations"]:
            if operation_yaml.get("extensions", {}).get("x-ms-long-running-operation"):
                operation = LROOperation.from_yaml(operation_yaml)
            elif operation_yaml.get("extensions", {}).get("x-ms-pageable"):
                operation = PagingOperation.from_yaml(operation_yaml)
            else:
                operation = Operation.from_yaml(operation_yaml)
            operations.append(operation)
            api_versions.update(operation.api_versions)

        return cls(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            class_name=yaml_data["language"]["python"]["className"],
            operations=operations,
            api_versions=api_versions
        )
