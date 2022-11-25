from pathlib import Path
import subprocess
import string
import random


seed = 985168183
random.seed(seed)
randint = random.randint

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "simple.py"

def write_test(name, times: list, hours: int):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{len(times)} {hours}\n")
        for time in times:
            file.write(f"{time}\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)


def make_random():
    n = randint(1, 15)
    h = randint(1, 10)

    times = []
    for _ in range(n):
        times.append(randint(1, 300))
    return times, h


def main():
    index = 1

    sample_test_cases = [
        ([15, 27, 5, 44], 1),
        ([240], 1),
        ([1], 1),
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", *inputs)
        index += 1

    tests_to_be_created = {
        make_random: 100,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__[5:]
            write_test(f"{index:03}-{name}", *func())
            index += 1



if __name__ == "__main__":
    main()
