from pathlib import Path
import subprocess

import numpy as np
randint = np.random.randint

np.random.seed(237862429)

max_vol = 1000

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "dp.py"

def write_test(name, v, volume, value):
    assert len(volume) == len(value)
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{len(volume)} {v}\n")
        file.write(" ".join(map(str, list(volume))) + "\n")
        file.write(" ".join(map(str, list(value))) + "\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)


def make_random(vol1=1, vol2=max_vol):
    v = randint(1, max_vol)
    n = randint(1, 1000)
    volume = [randint(vol1, vol2) for _ in range(n)]
    value = [randint(1, 100) for _ in range(n)]
    return v, volume, value

def make_random_small_vol():
    return make_random(vol2=50)

def make_random_very_small_vol():
    return make_random(vol2=2)

def make_random_large_vol():
    return make_random(vol1=int(max_vol * 0.95))

def main():
    index = 1

    sample_test_cases = [
        (21, [10, 17, 13, 5], [2, 18, 3, 16]),
        (max_vol, [max_vol - 5, 4, 4, 2, 2], [1, 30, 31, 20, 19]),
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", *inputs)
        index += 1

    tests_to_be_created = {
        make_random: 30,
        make_random_small_vol: 20,
        make_random_very_small_vol: 40,
        make_random_large_vol: 20,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__[5:]
            write_test(f"{index:03}-{name}", *func())
            index += 1

    custom_test_cases = [
        (max_vol, [1] * 1000, [1] * 1000),
        (max_vol, [max_vol] * 1000, [1] * 1000),
        (max_vol, [max_vol] * 1000, [100] * 1000),
        (max_vol, [1] * 1000, [100] * 1000),
    ]

    for inputs in custom_test_cases:
        write_test(f"{index:03}-edge-cases", *inputs)
        index += 1


if __name__ == "__main__":
    main()
