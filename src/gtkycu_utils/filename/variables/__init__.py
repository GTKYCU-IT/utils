from gtkycu_utils.filename.variables._registry import _register_variable_type, _variable_type_registry
from gtkycu_utils.filename.variables._registry import Variable
from gtkycu_utils.filename.variables._timestamp import _TimestampVariable
from gtkycu_utils.filename.variables._uuid4 import _UUID4Variable

_register_variable_type("timestamp.today", _TimestampVariable)
_register_variable_type("uuid.uuid4", _UUID4Variable)

def create_variable(variable_type: str, args: dict[str, str]) -> Variable:
    variable_cls = _variable_type_registry.get(variable_type)
    if variable_cls is None:
        raise ValueError("Unsupported variable data type")

    return variable_cls(**args)