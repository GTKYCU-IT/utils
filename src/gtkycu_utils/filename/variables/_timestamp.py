from gtkycu_utils.filename.variables._registry import Variable


from datetime import datetime


class _TimestampVariable(Variable):
    _format: str

    def __init__(self, format: str) -> None:
        self._format = format

    def get_value(self) -> str:
        return datetime.now().strftime(self._format)