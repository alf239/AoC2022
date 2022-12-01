fn main() {
    let raw_input = std::fs::read_to_string("./input_01.txt").expect("failed to read input");
    let input: Vec<&str> = raw_input.lines().collect();
    let mut elves: Vec<i64> = input.split(|s| s.is_empty())
                .map(|elf| elf.iter().map(|s| s.parse::<i64>().expect("no snack"))
                                .sum())
                .collect();
    let task1 = elves.iter().max().expect("Couldn't find max");
    println!("Task 1: {}", task1);
    elves.sort();
    let top3 = elves.as_slice()[elves.len() - 3..].to_vec();
    let task2: i64 = top3.iter().sum();
    println!("Task 2: {}", task2);
}
