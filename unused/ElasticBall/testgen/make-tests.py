from pathlib import Path
import random
import subprocess
import string

import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

randint = np.random.randint

seed = 43102220
random.seed(seed)
np.random.seed(seed)

parent_dir = Path(__file__).absolute().parent.parent
solution_path = parent_dir / "solutions" / "bfs.py"
assert solution_path.exists()

def write_test(name, maze: str):
    test_path = parent_dir / "tests" / f"{name}.in"
    maze = maze.strip().replace(' ', '')
    with open(test_path, 'w') as file:
        print(f"Creating test case {name}:", end="", flush=True)
        rows = maze.count('\n') + 1
        cols = maze.index('\n')
        file.write(f"{rows} {cols}\n")
        file.write(f"{maze}")
        print(f" | ✅ {name}.in ({rows=} {cols=})", end="", flush=True)
    ans_path = test_path.parent / f"{name}.ans"
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(ans_path)])
    subprocess.run(command, shell=True)
    ans = ans_path.open().read().strip()
    print(f" | ✅ {name}.ans (ans={ans})")


def make_random(max_size=False):
    pass

def get_sample1():
    # * will be replaced
    return """
    .....*............
    ....*.*...........
    ....*.*....*......
    ...*...*..*.*.....
    ...*...*..*.*..FF.
    ...*...*.*...*.FF.
    .SS.....**...**...
    .SS.....**...**...
    ##################
    """


def get_sample2():
    return """
    SS............
    SS............
    ..*...*.......
    ..*..*.*......
    ..*..*.*......
    ...**...*..*..
    ...**...*.*.*.
    ...**...*.*.**
    ...#.....#..#F
    """


def main():
    index = 1

    sample_test_cases = [
        get_sample1(),
        get_sample2(),
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", inputs)
        index += 1

    tests_to_be_created = {
        make_random: 100,
        make_random_max: 20,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__.replace("make_", "")
            write_test(f"{index:03}-{name}", func())
            index += 1


if __name__ == "__main__":
    main()
