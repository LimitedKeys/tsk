
import os
import subprocess

import pytest

PATH_HERE = os.path.dirname(__file__)
ROOT_PATH = os.path.abspath(
        os.path.join(PATH_HERE, ".."))
EXAMPLE_PATH = os.path.join(ROOT_PATH,
        "example")
TSK_PATH = os.path.join(ROOT_PATH, 
        "tsk.py")

EXAMPLES = [
    (os.path.join(EXAMPLE_PATH, "plan_a.md"), 
        b"Time: 1 w 2 d 2 h"),
    (os.path.join(EXAMPLE_PATH, "plan_b.md"), 
        b"Time: 1 y 6 w 2 d 6 h"),
]

def run(some_file):
    out = subprocess.run(
            [f"python {TSK_PATH} {some_file}"],
            shell=True,
            check=True,
            capture_output=True,
        )
    return out.stdout.strip()

@pytest.mark.parametrize("path,expected", EXAMPLES)
def test_cli_plan_a(path, expected):
    actual = run(path)
    assert actual == expected
