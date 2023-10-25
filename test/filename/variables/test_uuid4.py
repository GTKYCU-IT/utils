import uuid

from gtkycu_utils.filename.variables._uuid4 import _UUID4Variable


def test_value_is_uuid():
    variable = _UUID4Variable()
    uuid.UUID(variable.get_value(), version=4)
