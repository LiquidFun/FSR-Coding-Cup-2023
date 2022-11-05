from pathlib import Path
import subprocess
import string
import random


seed = 985297554
random.seed(seed)
randint = random.randint

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "greedy.py"

def write_test(name, w, n1, n2, n4):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{w}\n")
        file.write(f"{n1} {n2} {n4}\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)

def multirandint(*args):
    tuples = []
    for lo, hi in args:
        tuples.append(randint(lo, hi))
    return tuple(tuples)
        

def make_random():
    return multirandint((1, 1e9), (0, 1e9), (0, 1e9), (0, 1e9))

def make_random_zeros():
    while True:
        r = [random.random() < .4 for _ in range(3)]
        if any(a == 0 for a in r) and not all(a == 0 for a in r):
            break
    return multirandint((1, 1e9), (0, 1e9 * r[0]), (0, 1e9 * r[1]), (0, 1e9 * r[2]))

def make_random_small_width():
    return multirandint((1, 1e2), (0, 1e9), (0, 1e9), (0, 1e9))

def main():
    index = 1

    sample_test_cases = [
        (7, 5, 3, 1),
        (5, 3, 0, 500),
        (int(1e9), 0, 0, int(1e9) - 1),
        (1, 0, 0, 0),
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", *inputs)
        index += 1

    tests_to_be_created = {
        make_random: 50,
        make_random_zeros: 50,
        make_random_small_width: 50,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__[5:]
            write_test(f"{index:03}-{name}", *func())
            index += 1



if __name__ == "__main__":
    main()
