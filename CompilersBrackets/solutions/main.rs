// Author: Nick Kotsakidis
use std::io;

fn main() {
    let input = parse();
    let result = calc(&input);

    if result {
        println!("valid");
    } else {
        println!("invalid");
    }
}

fn parse() -> String {
    let mut input = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut input).unwrap();
    input
}

fn calc(input: &str) -> bool {
    let mut count = 0;
    for char in input.trim().chars() {
        match char {
            '{' => count += 1,
            '}' => count -= 1,
            _ => panic!("wrong bracket"),
        }
        if count < 0 {
            return false;
        }
    }

    count == 0
}
