#!/usr/bin/python

''' tsk: Simple Time Estimate

``` bash
> cat plan.md
# A
## A.1
Time: 2h
## A.2
Time: 24h

> tsk plan.md
Time: 1d 2h
'''

import re
import glob
import argparse

RE_TASK = re.compile(r'^#+ (.+)')

RE_TIME = re.compile(r'^TIME: (.+)', re.I)
RE_TAG = re.compile(r'^TAGS?: (.+)', re.I)

RE_HOURS = re.compile(r'(\d+) ?([ywdh]{1})', 
                      re.I)
HOURS_PER_HOUR = 1
HOURS_PER_DAY  = 8
HOURS_PER_WEEK = 40
HOURS_PER_YEAR = 52 * HOURS_PER_WEEK

UNITS = {
        'h': HOURS_PER_HOUR,
        'H': HOURS_PER_HOUR,
        'd': HOURS_PER_DAY,
        'D': HOURS_PER_DAY,
        'w': HOURS_PER_WEEK,
        'W': HOURS_PER_WEEK,
        'y': HOURS_PER_YEAR,
        'Y': HOURS_PER_YEAR,
        }

class TimeResult(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

def parse(*paths):
    ''' Parse the provided file, find task /
    time and return information.

    Args:
        *paths (str): path to files

    Returns:
        Dictionary of Tasks: {time: X}
    '''
    tasks = TimeResult()
    for path in paths:
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
                    tasks[name].time = str_to_hours(estimate)

                tag_match = RE_TAG.match(line)
                if tag_match:
                    estimate = tag_match.group(1)
                    if name not in tasks:
                        tasks[name] = TimeResult()
                    tasks[name].tag = estimate.strip()

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

def hours_to_str(value):
    '''Convert the input float hours into a 
    string.

    Args:
        valur (float): Number of hours

    Returns:
        String
    '''
    output = []

    if value >= HOURS_PER_YEAR:
        years = value // HOURS_PER_YEAR
        value -= years * HOURS_PER_YEAR
        output.append(f"{int(years)} y")

    if value >= HOURS_PER_WEEK:
        weeks = value // HOURS_PER_WEEK
        value -= weeks * HOURS_PER_WEEK
        output.append(f"{int(weeks)} w")

    if value >= HOURS_PER_DAY:
        days = value // HOURS_PER_DAY
        value -= days * HOURS_PER_DAY
        output.append(f"{int(days)} d")

    if value >= HOURS_PER_HOUR:
        hours = value // HOURS_PER_HOUR
        value -= hours * HOURS_PER_HOUR
        output.append(f"{int(hours)} h")

    return ' '.join(output)

def main():
    parser = argparse.ArgumentParser("tsk - Simple time estimate")
    parser.add_argument('path', help="path to the markdown file (glob ok)")
    parser.add_argument('--list', help="list the task and times", action='store_true')
    parser.add_argument('--csv', help="output as csv format", action='store_true')
    parser.add_argument('--tag', help="only show items from selected tag", default="", type=str)

    args = parser.parse_args()
    paths = glob.glob(args.path)
    result = parse(*paths)

    total = 0
    summary = []
    for (k, v) in result.items():
        if args.tag:
            if "tag" not in v:
                continue
            if args.tag not in v.tag:
                continue

        if "tag" in v:
            summary.append(
                (v.tag, k, v.time)
                )
        else:
            summary.append(
                ('', k, v.time)
                )
        total += v.time

    summary.sort()
    if args.csv:
        print("Tag, Name, Hours,")
        for tag, name, hours in summary:
            print(f'"{tag}", "{name}", {hours},')
        return

    print(f"Time: {hours_to_str(total)}")

    if args.list:
        print("---")
        for i, (tag, name, hours) in enumerate(summary, 1):
            if tag:
                print(f'{i}. <{tag}> {name}: {hours_to_str(hours)}')
            else:
                print(f'{i}. {name}: {hours_to_str(hours)}')


if __name__ == '__main__':
    main()
