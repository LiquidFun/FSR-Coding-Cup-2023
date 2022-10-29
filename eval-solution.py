#!/bin/python3

"""
This file can be used to test solutions. It clones the scripts submodule and then tests the most recent solution
matching the given pattern.
"""

import os
import sys
from pathlib import Path
from subprocess import run
import argparse

ignore_dirs = ["scripts"]

repo_path = Path(__file__).absolute().parent 
program_tester_path = repo_path / "scripts" / "program-tester.sh"

def candidate_solution_paths(pattern: str) -> list[Path]:
    solution_paths = []
    if pattern != "" and (pattern_path := Path(pattern)).exists():
        if pattern_path.is_file():
            solution_paths.append(pattern_path)
        if pattern_path.is_dir():
            solution_paths.extend(pattern_path.glob("solutions/*"))
    else:
        cwd = Path().cwd()
        os.chdir(repo_path)
        for path in Path.cwd().iterdir():
            if path.name not in ignore_dirs:
                if path.is_dir() and (path / "solutions").exists():
                    solution_paths.extend(path.glob("solutions/*"))
        os.chdir(cwd)
    return solution_paths


def init_submodule() -> None:
    cwd = Path.cwd().absolute()
    os.chdir(repo_path)
    if not program_tester_path.exists():
        run("git submodule init", shell=True)
    run("git submodule update", shell=True)
    os.chdir(cwd)

def as_tests_pattern(path) -> str:
    return str(path.parent.parent / "tests") + "/*.in"

def print_message(path, state="", use_colors=True):
    color1 = "\033[31m" if use_colors else ""
    color2 = "\033[32m" if use_colors else ""
    bold = "\033[1m" if use_colors else ""
    reset = "\033[0m" if use_colors else ""
    print(f"=== {color2}{state}{reset} Testing solution {color1}{path.name}{reset} in problem {bold}{color2}{path.parents[1].name}{reset} ===\n")


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("pattern", default="", nargs="?", help="Pattern which will used to find candidate solution to test (can be exact filepath).")
    argparser.add_argument("-a", "--all", action="store_true", help="Test on all solutions instead of most recent one")
    argparser.add_argument("-s", "--summary", action="store_true", help="Only print a summary of the test cases of each solution")
    args = argparser.parse_args()
    init_submodule()
    solutions = candidate_solution_paths(args.pattern)
    if not args.all:
        solutions = sorted(solutions, key=lambda p: p.stat().st_mtime)[-1:]
    for solution in solutions:
        print_message(solution)
        run([
            str(program_tester_path),
            str(solution),
            "-p",
            as_tests_pattern(solution),
            "-s" if args.summary else "",
            "-c" if sys.platform != "win32" else "",
        ])
        print_message(solution, "COMPLETED")

    

if __name__ == "__main__":
    main()
