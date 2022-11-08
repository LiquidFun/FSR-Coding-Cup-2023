from pathlib import Path
import subprocess
import string
import random
import numpy as np


seed = 985421069
np.random.seed(seed)
random.seed(seed)
randint = random.randint

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "simple.py"

def write_test(name, brackets: str):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{brackets}\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)

def shuffled(s):
    s = list(s)
    random.shuffle(s)
    return ''.join(s)
        
def make_random(equal=False):
    n = randint(1, 490)
    m = n if equal else randint(1, 490)
    return "{{{{{{{{" + shuffled("{" * n + "}" * m) + "}}}}}}}}"

def make_random_equal():
    return make_random(True)

def make_open_closed():
    n = randint(1, 500)
    return "{}" * n

def make_open_closed_deep():
    n = randint(1, 500)
    return "{" * n + "}" * n

def main():
    index = 1

    sample_test_cases = [
        "{{}}{}",
        "{}{}{{}}}",
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", inputs)
        index += 1

    tests_to_be_created = {
        make_random: 10,
        make_random_equal: 70,
        make_open_closed: 3,
        make_open_closed_deep: 3,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__[5:]
            write_test(f"{index:03}-{name}", func())
            index += 1

    edge_test_cases = [
        "{",
        "}",
        "{}",
        "}{",
    ]

    for inputs in edge_test_cases:
        write_test(f"{index:03}-edgecase", inputs)
        index += 1



if __name__ == "__main__":
    main()
