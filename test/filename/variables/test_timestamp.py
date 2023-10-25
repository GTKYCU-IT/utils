import pytest
from gtkycu_utils.filename import FilenameGenerator


import datetime
import os


def test_filename_with_timestamp(dt_fmt: str, filename: str):
    template = r"filename-{today}.txt"
    variable_configs = [
        {"name": "today", "type": "timestamp.today", "args": {"format": dt_fmt}}
    ]
    filename_generator = FilenameGenerator(variable_configs=variable_configs)

    expected = template.format(today=datetime.datetime.now().strftime(dt_fmt))
    result = filename_generator.generate(template)
    assert result == expected


@pytest.fixture(params=["my_file.txt", "FILE", "my.file.name.txt"])
def filename(request):
    yield request.param


@pytest.fixture(params=["%Y", "%Y-%m-%d", "%Y-%m-%d_%H:%M"])
def dt_fmt(request):
    yield request.param
