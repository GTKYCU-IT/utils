from gtkycu_utils.filename.variables._registry import Variable


import uuid


class _UUID4Variable(Variable):
    def get_value(self) -> str:
        return str(uuid.uuid4())