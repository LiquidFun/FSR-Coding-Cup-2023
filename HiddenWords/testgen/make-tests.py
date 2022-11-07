from pathlib import Path
import subprocess
import string
import random
import numpy as np


seed = 985297554
np.random.seed(seed)
random.seed(seed)
randint = random.randint

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "simple.py"

def write_test(name, words: list[str]):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{len(words)}\n")
        file.write(' '.join(words) + "\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)
        
def random_word():
    n = randint(1, 50)
    allowed = list(string.ascii_lowercase)
    return ''.join(np.random.choice(allowed, n, replace=True))

def make_random():
    n = randint(1, 1000)
    return [random_word() for _ in range(n)]

def make_random_correlated():
    words = [random_word()]
    n = randint(1, 1000) - 1
    for _ in range(n):
        correlation = randint(0, len(words[-1]))
        new_word = (words[-1][len(words[-1])-correlation:] + random_word())[:50]
        words.append(new_word)
    return words

def make_single_letter():
    return ["a"]

def make_single_letter_multi():
    return ["z"] * 1000

def make_random_same_word_only():
    return [random_word()] * randint(1, 1000)

def main():
    index = 1

    sample_test_cases = [
        "in inter intercontinental continentally tallying unrelated".split(),
        "at bat attack king".split(),
    ]

    for inputs in sample_test_cases:
        write_test(f"{index:03}-sample", inputs)
        index += 1

    tests_to_be_created = {
        make_random: 40,
        make_random_correlated: 40,
        make_random_same_word_only: 10,
        make_single_letter: 1,
        make_single_letter_multi: 1,
    }

    for func, how_many in tests_to_be_created.items():
        for _ in range(how_many):
            name = func.__name__[5:]
            write_test(f"{index:03}-{name}", func())
            index += 1



if __name__ == "__main__":
    main()
