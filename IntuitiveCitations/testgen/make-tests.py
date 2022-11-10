from pathlib import Path
import subprocess
import string
import random

import numpy as np


seed = 638988505
random.seed(seed)
randint = random.randint
np.random.seed(seed)

letters = list(string.ascii_letters)

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "simple.py"

def write_test(name, authors: list):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{len(authors)}\n")
        for author in authors:
            file.write(f"{author}\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)


def random_word():
    n = randint(2, 20)
    return ''.join(np.random.choice(letters, n)).title()


def make_random():
    n = randint(1, 20)
    authors = []
    for _ in range(n):
        authors.append(random_word() + " " + random_word())
    return authors


def main():
    index = 1

    sample_test_cases = [
        [
            "Donald Knuth",
            "Edsger Dijkstra",
            "Allen Newell",
            "Ken Thompson",
        ],
        [
            "Alan Turing",
        ],
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", inputs)
        index += 1

    tests_to_be_created = {
        make_random: 100,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__[5:]
            write_test(f"{index:03}-{name}", func())
            index += 1



if __name__ == "__main__":
    main()
