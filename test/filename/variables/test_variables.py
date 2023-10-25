import pytest

from gtkycu_utils.filename import FilenameGenerator
from gtkycu_utils.filename.variables import Variable, _register_variable_type


class MockVariable(Variable):
    _my_arg: str

    def __init__(self, my_arg = "value") -> None:
        self._my_arg = my_arg
        
    def get_value(self) -> str:
        return f"mock_{self._my_arg}"

@pytest.fixture
def register_mock_variable_type():
    _register_variable_type("test", MockVariable)
    yield

@pytest.fixture(params=[
    {"name": "test_var", "type": "test", "args": { "my_arg": "apple" }},
    {"name": "my_test", "type": "test", "args": { "my_arg": "banana" }},
    {"name": "TESTVAR", "type": "test", "args": { "my_arg": "coconut" }},
    {"name": "my_variable", "type": "test", "args": { "my_arg": "donut" }},
])
def timestamp_variable_config(request):
    yield request.param

@pytest.mark.usefixtures("register_mock_variable_type")
def test_timestamp_different_variable_names(timestamp_variable_config):
    template = f"{{{timestamp_variable_config["name"]}}}"
    variable_configs = [timestamp_variable_config]
    filename_generator = FilenameGenerator(variable_configs=variable_configs)

    expected = f"mock_{timestamp_variable_config.get("args")["my_arg"]}"
    result = filename_generator.generate(template)
    assert result == expected


def test_bad_variable_type_raises_value_error():
    with pytest.raises(ValueError, match="Unsupported variable data type"):
        filename_generator = FilenameGenerator(variable_configs=[{"type": "unsupported"}])
