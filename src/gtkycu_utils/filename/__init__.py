from collections import defaultdict
import os

from gtkycu_utils.filename.variables import create_variable


class FilenameGenerator:
    _variables: dict[str, str]

    def __init__(self, variable_configs: list[dict[str, str]]) -> None:
        self._variables = defaultdict(str)
        for c in variable_configs:
            name = c.get("name")
            variable = create_variable(
                variable_type=c.get("type"), args=c.get("args", {})
            )
            self._variables[name] = variable.get_value()

    def generate(self, filename_template: str) -> str:
        return filename_template.format_map(
            defaultdict(str, **self._variables)
        )
