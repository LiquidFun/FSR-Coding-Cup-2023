// Author: Nick Kotsakidis
use std::io;

fn main() {
    let (mut start, target) = parse();
    let result = calc(&mut start, &target);

    if let Some(turns) = result {
        println!("{turns}");
    } else {
        println!("impossible");
    }
}

fn parse() -> (Vec<i8>, Vec<i8>) {
    let mut input = String::new();
    let mut start = String::new();
    let mut target = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut input).unwrap();
    stdin.read_line(&mut start).unwrap();
    stdin.read_line(&mut target).unwrap();

    let start = start
        .split(" ")
        .map(|s| s.trim().parse::<i8>().unwrap())
        .collect::<Vec<_>>();
    let target = target
        .split(" ")
        .map(|s| s.trim().parse::<i8>().unwrap())
        .collect::<Vec<_>>();

    (start, target)
}

fn calc(start: &mut Vec<i8>, target: &Vec<i8>) -> Option<usize> {
    let mut turns = 0;
    let last = start.len() - 1;

    for i in 0..last {
        let mut distance = start[i] - target[i];
        if distance.abs() > 5 {
            let old_distance = distance;
            distance = 10 - distance.abs();
            if old_distance.is_positive() {
                distance = distance * -1;
            }
        }

        start[i] = start[i] - distance;
        start[i + 1] = start[i + 1] - distance;

        if start[i] < 0 {
            start[i] = 10 + start[i];
        }
        if start[i + 1] < 0 {
            start[i + 1] = 10 + start[i + 1];
        }

        if start[i] > 9 {
            start[i] -= 10;
        }
        if start[i + 1] > 9 {
            start[i + 1] -= 10;
        }

        turns += distance.abs() as usize;
    }

    if start[last] == target[last] {
        Some(turns)
    } else {
        None
    }
}
