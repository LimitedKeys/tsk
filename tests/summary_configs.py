
SUMMARY_1 = [
    # path, tag, name, time
    ("a.md", "", "1", 1),
    ("b.md", "1", "2", 2),
    ("b.md", "2", "abc", 1),
    ("c.md", "a", "1", 4),
    ("d.md", "x", "2", 1),
]

TOTAL_1 = {
    "":1,
    "1":2,
    "2":1,
    "a":4,
    "x":1,
    "total":9,
}

TOTAL_1A = {
    "a":4,
    "total":4,
}

SUMMARY_2 = [
    # path, tag, name, time
    ("a/b.md", "123", "first", 12),
    ("a/b.md", "123", "second", 23),
    ("a/b.md", "123", "third", 11),
    ("a/b.md", "34", "fifth", 13),
    ("a/b.md", "34", "fourth", 12),
]

TOTAL_2 = {
    "123":46,
    "34":25,
    "total":71,
}

TOTAL_2A = {
    "123":46,
    "total":46
}

TOTAL_2B = {
    "34":25,
    "total":25,
}

TOTAL_2C = {
    "123":46,
    "34":25,
    "total":71,
}

CONFIGS = [
    (SUMMARY_1, TOTAL_1, None),
    (SUMMARY_1, TOTAL_1A, "a"),
    (SUMMARY_2, TOTAL_2, None),
    (SUMMARY_2, TOTAL_2A, "123"),
    (SUMMARY_2, TOTAL_2B, "34"),
    (SUMMARY_2, TOTAL_2C, "3"),
]
