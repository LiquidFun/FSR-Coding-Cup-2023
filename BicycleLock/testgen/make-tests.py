from pathlib import Path
import subprocess

import numpy as np
randint = np.random.randint

np.random.seed(237859234)

def solve(current, target):
    current = list(current)
    total = 0
    for i in range(len(current)-1):
        diff = target[i] - current[i]
        total += min(10 - abs(diff), abs(diff))
        current[i+1] = (current[i+1] + diff) % 10
        
    return total if current[-1] == target[-1] else "impossible"

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "simple.py"

def write_test(name, current, target):
    assert len(current) == len(target)
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{len(current)}\n")
        file.write(" ".join(map(str, list(current))) + "\n")
        file.write(" ".join(map(str, list(target))) + "\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)


def make_random():
    n = randint(2, 101)
    return randint(0, 10, n), randint(0, 10, n)

def make_random_possible():
    current, target = make_random()
    current = list(current)
    while solve(current, target) == "impossible":
        current[-1] = (current[-1] + 1) % 10
    assert solve(current, target) != "impossible"
    return current, target


def make_all_same():
    n = randint(2, 101)
    return [randint(10)] * n, [randint(10)] * n


def make_add_m():
    n = randint(2, 101)
    m = randint(10)
    current = np.randint(0, 10, n)
    return current, (current + m) % 10
    

def main():
    tests_to_be_created = {
        make_random: 30,
        make_all_same: 12,
        make_random_possible: 20,
    }
    
    for func, how_many in tests_to_be_created.items():
        for i in range(1, how_many+1):
            name = func.__name__[5:]
            write_test(f"{i:02}-{name}", *func())

    custom_test_cases = [
        ([0, 9], [9, 0]),
        ([9, 9], [0, 0]),
        ([9, 9, 9], [0, 0, 0]),
        ([9, 9, 0, 0], [0, 0, 8, 8]),
    ]

    for i, inputs in enumerate(custom_test_cases):
        write_test(f"{i+1:02}-edge-cases", *inputs)

    sample_test_cases = [
        ([1, 4, 6, 1, 3], [6, 4, 2, 3, 4]),
        ([9, 0], [5, 6]),
        ([9, 0, 1], [5, 6, 2]),
    ]

    for i, inputs in enumerate(sample_test_cases):
        write_test(f"{i+1:02}-sample", *inputs)


if __name__ == "__main__":
    main()
