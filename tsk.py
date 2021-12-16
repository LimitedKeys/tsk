import re

RE_TASK = re.compile(r'^#+ (.+)')
RE_TIME = re.compile(r'^TIME: (.+)', re.I)

class TimeResult(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

def parse(path):
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
