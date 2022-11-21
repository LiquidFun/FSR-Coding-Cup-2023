// Author: Nick Kotsakidis
use std::io;

fn main() {
    let input = parse();
    let r = calc(input);

    print!("{r}\n");
}

fn parse() -> Vec<String> {
    let mut str = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut str).unwrap();
    str.clear();
    stdin.read_line(&mut str).unwrap();
    let input = str.split(" ").map(|s| s.parse().unwrap()).collect();

    input
}

fn intersection(a: &str, b: &str) -> usize {
    let la = a.len();
    let lb = b.len();
    let l = la.min(lb);

    for i in (0..l).rev() {
        let ta = &a[(la - i - 1)..];
        let tb = &b[..=i];
        if ta == tb {
            return i + 1;
        }
    }
    0
}

fn calc(input: Vec<String>) -> String {
    let mut r = String::new();

    let mut last = String::new();
    for i in input {
        let c = intersection(&last, &i);
        r.push_str(&i[c..]);
        last = i;
    }

    r
}
