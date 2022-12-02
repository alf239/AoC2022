fn score(c: char) -> u32 {
    match c {
        'A' => 1,
        'B' => 2,
        'C' => 3,
        'X' => 1,
        'Y' => 2,
        'Z' => 3,
        _ => 0
    }
}

fn side(s: &str, idx: usize) -> u32 {
    score(s.chars().nth(idx).unwrap())
}

fn you(s: &str) -> u32 {
    side(s, 2)
}

fn elf(s: &str) -> u32 {
    side(s, 0)
}

fn outcome1(s: &str) -> u32 {
    let y = you(s);
    let e = elf(s);
    let round = if y == e {
        3
    } else if y % 3 == (e + 1) % 3 {
        6
    } else {
        0
    };
    y + round
}

fn outcome2(s: &str) -> u32 {
    let e = elf(s);
    match you(s) {
        1 => (e + 1) % 3 + 1, 
        2 => 3 + e,
        3 => 6 + e % 3 + 1,
        _ => 0
    }
}

fn final_score(input: &[&str], f: fn(&&str) -> u32) -> u32 {
    input.iter().map(f).sum()
}

fn main() {
    let raw_input = std::fs::read_to_string("./input_02.txt").expect("failed to read input");
    let input: Vec<&str> = raw_input.lines().collect();
    let task1: u32 = final_score(input.as_slice(), |s| outcome1(s));
    println!("Task 1: {}", task1);

    let task2: u32 = final_score(input.as_slice(), |s| outcome2(s));
    println!("Task 2: {}", task2);
}
