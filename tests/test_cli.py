
import os
import sys
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
    (os.path.join(EXAMPLE_PATH, "plan_c.md"), 
        b"Time: 3 h"),
]

TAG_EX = [
    (os.path.join(EXAMPLE_PATH, "plan_c.md"), 
        "test",
        b"Time: 1 h"),
]

def run(some_file, tag=None):
    command = [
        f"{sys.executable}",
        f"{TSK_PATH}",
        f"{some_file}",
    ]
    if tag:
        command.append("--tag")
        command.append(f"{tag}")

    out = subprocess.run(
            command,
            check=True,
            capture_output=True,
        )
    return out.stdout.strip()

@pytest.mark.parametrize("path,expected", EXAMPLES)
def test_cli(path, expected):
    actual = run(path)
    assert actual == expected

@pytest.mark.parametrize("path,tag,expected", TAG_EX)
def test_cli_tag(path, tag, expected):
    actual = run(path, tag=tag)
    assert actual == expected
