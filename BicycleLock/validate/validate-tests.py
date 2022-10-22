from pathlib import Path

tests_path = Path(__file__).absolute().parent.parent / "tests"

for test_path in sorted(tests_path.glob("*.in")):
    with open(test_path) as file:
        n, current, target = file.readlines()
        n = int(n)
        current = list(map(int, current.split()))
        target = list(map(int, target.split()))
        assert n == len(current) == len(target)
        assert all(0 <= a <= 9 for a in (target + current))
        print(test_path.name, " is good!")


for test_path in sorted(tests_path.glob("*.ans")):
    with open(test_path) as file:
        answer = file.read().strip()
        if answer != "impossible":
            int(answer)
        print(test_path.name, " is good!")
