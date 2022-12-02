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

fn outcome1(s: &str) -> u32 {
    let you = score(s.chars().nth(2).unwrap());
    let elf = score(s.chars().nth(0).unwrap());
    let round = if you == elf {
        3
    } else if you % 3 == (elf + 1) % 3 {
        6
    } else {
        0
    };
    you + round
}

fn outcome2(s: &str) -> u32 {
    let you = s.chars().nth(2).unwrap();
    let elf = score(s.chars().nth(0).unwrap());
    match you {
        'X' => (elf + 1) % 3 + 1, 
        'Y' => 3 + elf,
        'Z' => 6 + elf % 3 + 1,
        _ => 0
    }
}

fn main() {
    let raw_input = std::fs::read_to_string("./input_02.txt").expect("failed to read input");
    let input: Vec<&str> = raw_input.lines().collect();
    let task1: u32 = input.iter().map(|s| outcome1(s)).sum();
    println!("Task 1: {}", task1);

    let task2: u32 = input.iter().map(|s| outcome2(s)).sum();
    println!("Task 2: {}", task2);
}
