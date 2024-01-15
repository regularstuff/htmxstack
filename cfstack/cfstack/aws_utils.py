import json

from django.conf import settings
import pathlib

def get_stack_names():
    base_dir = settings.BASE_DIR
    stacks_path = pathlib.Path(base_dir, "aws_mock_stacks")
    return [file.name for file in stacks_path.glob("*json")]

def get_stack_as_dict(stack_name):
    base_dir = settings.BASE_DIR
    stacks_path = pathlib.Path(base_dir, "aws_mock_stacks")
    with open((stacks_path / stack_name).absolute()) as stack_file:
        return json.load(stack_file)



