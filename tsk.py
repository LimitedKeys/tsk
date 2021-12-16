#!/usr/bin/python
''' tsk: Simple Time Estimate

> tsk plan.md
Time: 1d 2h
'''

import re

RE_TASK = re.compile(r'^#+ (.+)')
RE_TIME = re.compile(r'^TIME: (.+)', re.I)
RE_HOURS = re.compile(r'(\d+) ?([ywdh]{1})', 
                      re.I)

UNITS = {
        'h': 1,
        'H': 1,
        'd': 8,
        'D': 8,
        'w': 40,
        'W': 40,
        'y': 52*40,
        'Y': 52*40,
        }

class TimeResult(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

def parse(path):
    ''' Parse the provided file, find task /
    time and return information.

    Args:
        path (str): path to file

    Returns:
        Dictionary of Tasks: {time: X}
    '''
    tasks = TimeResult()
    with open(path, 'r') as plan:
        name = None
        for line in plan:
            task_match = RE_TASK.match(line)
            if task_match:
                name = task_match.group(1)

            time_match = RE_TIME.match(line)
            if time_match:
                estimate = time_match.group(1)
                if name not in tasks:
                    tasks[name] = TimeResult()
                tasks[name].time = estimate

    return tasks

def str_to_hours(value):
    '''Convert the input string into hours.

    Args:
        value (str): Time string (y w d h)

    Returns:
        Hours as a float
    '''
    total = 0
    for m in RE_HOURS.finditer(value):
        value = m.group(1)
        unit = m.group(2)

        total += float(value) * UNITS[unit]

    return total
