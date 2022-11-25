// Author: Nick Kotsakidis
use std::io;

#[derive(Debug)]
struct Input {
    a: f64,
    b: f64,
    c: f64,
}

fn main() {
    let input = parse();
    let r = calc(input);

    print!("{r}\n");
}

fn parse() -> Input {
    let mut str = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut str).unwrap();
    let cache = str.split(" ").collect::<Vec<_>>();

    let mut input = Input {
        a: cache[0].trim().parse().unwrap(),
        b: cache[1].trim().parse().unwrap(),
        c: cache[2].trim().parse().unwrap(),
    };

    input.b *= 0.1;
    input.c *= 0.1;

    input
}

fn compound_interest(k0: f64, n: i32, p: f64) -> f64 {
    k0 * ((100. + p) / 100.).powi(n)
}

fn calc(input: Input) -> f64 {
    let mut max = 0.;
    for i in 0..=365 {
        let n = i;
        let a = 365 - i;
        let new = compound_interest(input.a, n, input.b);
        let new1 = compound_interest(new, a, -input.c);

        if new1 > input.a {
            // println!("{},{},{}", a, new, new1);
            let max_neu = new - new1;
            if max_neu > max {
                max = max_neu;
            } else {
                break;
            }
        }
    }
    max
}
