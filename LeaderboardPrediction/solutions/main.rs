// Author: Nick Kotsakidis
use std::io;

#[derive(Debug)]
struct Input {
    problem_count: usize,
    duration: usize,
    problems: Vec<usize>,
}

fn main() {
    let input = parse();
    let (count, time) = calc(input);

    print!("{count} {time}\n");
}

fn parse() -> Input {
    let mut str = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut str).unwrap();
    let (problem_count, duarion) = str.split_once(" ").unwrap();
    let mut input = Input {
        problem_count: problem_count.trim().parse().unwrap(),
        duration: duarion.trim().parse().unwrap(),
        problems: vec![],
    };

    for _ in 0..input.problem_count {
        str.clear();
        stdin.read_line(&mut str).unwrap();
        input.problems.push(str.trim().parse().unwrap());
    }
    input
}

fn calc(mut input: Input) -> (usize, usize) {
    input.duration = input.duration * 60;
    input.problems.sort();

    let mut elapsed_time = 0;
    let mut count = 0;
    let mut penalty = 0;
    for i in input.problems.iter() {
        if elapsed_time + i <= input.duration {
            count += 1;
            elapsed_time += i;
            penalty += elapsed_time;
        }
    }

    (count, penalty)
}
