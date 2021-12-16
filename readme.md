# TSK - quick time estimate

Quickly estimate time using markdown:

~~~
> cat plan.md
# Project

Resources: 1

## One

Time: 100 h

## Two

Time: 23 h

> tsk plad.md
Time: 123 h
Resources: 1.0
~~~

## Details

This tool is to give the author a sense of how long the outlined project will take. The goal is not to:

- plan week by week
- allocate resources
- determine task dependence

just to estimate. Which is fine for a small project.

## Calculations

~~~
Project Time = Sum(Task Times) / Resources
~~~
