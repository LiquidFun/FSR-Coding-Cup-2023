from pathlib import Path
import subprocess
import random

randint = random.randint

random.seed(25114342)

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "simple.py"

def write_test(name, megafishes, growing, fishing):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{megafishes} {growing} {fishing}\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)


def make_random():
    return randint(1, 1000), randint(1, 50), randint(1, 999)


def main():
    index = 1

    sample_test_cases = [
        (2, 10, 20),
        (3, 50, 1),
        (1000, 50, 999),
        (4, 1, 999),
        (1, 1, 1),
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

    custom_test_cases = [
    ]

    for inputs in custom_test_cases:
        write_test(f"{index:03}-edge-cases", *inputs)
        index += 1


if __name__ == "__main__":
    main()
