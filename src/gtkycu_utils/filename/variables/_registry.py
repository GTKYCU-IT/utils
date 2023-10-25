from abc import ABC


class Variable(ABC):
    def get_value(self) -> str:
        """"""


_variable_type_registry: dict[str, type[Variable]] = {}


def _register_variable_type(variable_type: str, variable_cls: type[Variable]):
    _variable_type_registry[variable_type] = variable_cls
