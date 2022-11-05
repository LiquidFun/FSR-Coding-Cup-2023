from pathlib import Path
import subprocess
import string
import random
from itertools import combinations_with_replacement


seed = 1985168
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
    letters = string.ascii_lowercase + "_" + "." * (36 - 27)
    random.shuffle(letters)
    n = randint(1, 200)
    words = ''.join(combinations_with_replacement(string.ascii_lowercase + '_', n))
    return letters, words


def main():
    index = 1

    sample_test_cases = [
        (".rsft..qedu..pacih.zbmjg.yolkn._xwv.", "hello my great friend i have not seen you in a long time"),
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
