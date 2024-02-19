"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [(3, 6, 7, 4, 5, 1, 2)],
            "answer": 3,
        },
        {
            "input": [(6, 5, 4, 3, 2, 1)],
            "answer": 6,
        },
        {
            "input": [(5, )],
            "answer": 1,
        },
    ],
    "Extra": [
        {
            "input": [(1, 3, 2, 5, 4, 7, 6)],
            "answer": 2,
        },
        {
            "input": [(20, 48, 36, 42, 29, 30, 33, 97, 73, 69)],
            "answer": 3,
        },
        {
            "input": [(19, 51, 53, 2, 12, 57, 98, 42, 25, 56)],
            "answer": 2,
        },
        {
            "input": [(36, 94, 53, 31, 60, 82, 89, 73, 43, 47)],
            "answer": 4,
        },
    ]
}
