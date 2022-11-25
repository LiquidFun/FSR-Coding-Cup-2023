// Author: Nick Kotsakidis
use std::io;

fn main() {
    let (w, b1, b2, b4) = parse();
    let result = calc2(w, b1, b2, b4);

    println!("{result}");
}

fn parse() -> (usize, usize, usize, usize) {
    let mut input = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut input).unwrap();
    stdin.read_line(&mut input).unwrap();
    let input = input.lines().collect::<Vec<_>>();
    let w = input[0].trim().parse().unwrap();
    let b = input[1]
        .splitn(3, " ")
        .map(|s| s.parse().unwrap())
        .collect::<Vec<_>>();

    (w, b[0], b[1], b[2])
}

fn calc2(w: usize, mut b1: usize, mut b2: usize, mut b4: usize) -> usize {
    let mut height = 0;

    let mut complete = true;
    while complete {
        let mut w = w;
        let mut cb4 = 0;
        let mut cb2 = 0;
        let mut cb1 = 0;

        if b4 > 0 && w >= 4 {
            let max = (w / 4).min(b4);
            w -= max * 4;
            b4 -= max;
            cb4 = max;
        }
        if b2 > 0 && w >= 2 {
            let max = (w / 2).min(b2);
            w -= max * 2;
            b2 -= max;
            cb2 = max;
        }
        if b1 > 0 {
            let max = (w).min(b1);
            w -= max * 1;
            b1 -= max;
            cb1 = max;
        }

        if w == 0 {
            height += 1;
            let min = (b4.checked_div(cb4).unwrap_or(usize::MAX))
                .min(b2.checked_div(cb2).unwrap_or(usize::MAX))
                .min(b1.checked_div(cb1).unwrap_or(usize::MAX));
            if min > 0 {
                height += min;
                b4 -= cb4 * min;
                b2 -= cb2 * min;
                b1 -= cb1 * min;
            }
        } else {
            complete = false;
            // println!("{b4},{b2},{b1}");
        }
    }
    height
}

#[allow(dead_code)]
fn calc(w: usize, mut b1: usize, mut b2: usize, mut b4: usize) -> usize {
    let mut height = 0;

    let mut complete = true;
    while complete {
        let mut w = w;
        while w > 0 {
            if b4 > 0 && w >= 4 {
                w -= 4;
                b4 -= 1;
            } else if b2 > 0 && w >= 2 {
                w -= 2;
                b2 -= 1;
            } else if b1 > 0 {
                w -= 1;
                b1 -= 1;
            } else {
                break;
            }
        }
        if w == 0 {
            height += 1;
        } else {
            complete = false;
        }
    }

    height
}
