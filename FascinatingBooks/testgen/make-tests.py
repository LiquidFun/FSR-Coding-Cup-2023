from pathlib import Path
import subprocess
import string
import random


seed = 637872786
random.seed(seed)
randint = random.randint

letters = string.ascii_letters + ":' "

solution_path = Path(__file__).absolute().parent.parent / "solutions" / "simple.py"

def write_test(name, books: list):
    test_path = Path(__file__).absolute().parent.parent / "tests" / f"{name}.in"
    with open(test_path, 'w') as file:
        print(f"Test case {name} written!")
        file.write(f"{len(books)}\n")
        for book in books:
            file.write(f"{book}\n")
    command = ' '.join(["python", str(solution_path), "<", str(test_path), ">", str(test_path.parent / f"{name}.ans")])
    subprocess.run(command, shell=True)


def make_random():
    n = randint(2, 50)
    is_missing = random.random() < .4

    missing = random.choice(letters).lower() if is_missing else " "
    books = []
    for _ in range(n):
        chars = randint(2, 100)
        books.append(''.join(random.choice(letters) for _ in range(chars)))
        books[-1] = books[-1].replace(missing, " ").replace(missing.upper(), " ")
    return books


def main():
    index = 1

    sample_test_cases = [
        [
            "Visual Basic",
            "Introduction to Algorithms",
            "Computational Complexity",
            "Reviewing Java",
            "Exploring Requirements: Quality Before Design",
            "Structured Computer Organization",
            "Hacker's Delight",
        ],
        [
            "Introduction to Algorithms",
            "The C Programming Language",
            "Structured Computer Organization",
        ],
        [
            "Computational Complexity",
            "Waltzing with Bears: Managing Risk on Software Projects",
            "The Quark and the Jaguar: Adventures in the Simple and the Complex",
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
