// Author: Nick Kotsakidis
use std::{collections::VecDeque, io};

fn main() {
    let mut input = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut input).unwrap();
    let (rows, columns) = input.trim().split_once(" ").unwrap();
    let rows = rows.parse::<usize>().unwrap();
    let columns = columns.parse::<usize>().unwrap();

    input = String::with_capacity(rows * (columns + 2));
    for _ in 0..rows {
        stdin.read_line(&mut input).unwrap();
    }

    let result = calc(&input);
    let result = result.to_string() + ("\n");
    println!("{result}")
}

#[derive(Debug, PartialEq, Clone, Copy)]
enum Status {
    Wall,
    Air,
    Water,
}

fn calc(input: &str) -> usize {
    let mut avarium: Vec<Vec<Status>> = Vec::new();

    for line in input.lines() {
        let mut row = Vec::new();
        for char in line.chars() {
            match char {
                '#' => row.push(Status::Wall),
                '.' => row.push(Status::Air),
                _ => {
                    panic!("unsopported char")
                }
            }
        }
        avarium.push(row);
    }

    let mut liters = 0;

    let mut queue = VecDeque::new();
    for i in 0..avarium[0].len() {
        if avarium[0][i] == Status::Air {
            liters += 1;
            avarium[0][i] = Status::Water;

            if avarium[1][i] == Status::Air {
                queue.push_back((1 as usize, i));
                avarium[1][i] = Status::Water;
                liters += 1;
            }
        }
    }

    while let Some(p) = queue.pop_front() {
        if avarium[p.0][p.1 - 1] == Status::Air {
            queue.push_back((p.0, p.1 - 1));
            avarium[p.0][p.1 - 1] = Status::Water;
            liters += 1;
        }
        if avarium[p.0][p.1 + 1] == Status::Air {
            queue.push_back((p.0, p.1 + 1));
            avarium[p.0][p.1 + 1] = Status::Water;
            liters += 1;
        }
        if avarium[p.0 + 1][p.1] == Status::Air {
            queue.push_back((p.0 + 1, p.1));
            avarium[p.0 + 1][p.1] = Status::Water;
            liters += 1;
        }
    }

    liters
}
