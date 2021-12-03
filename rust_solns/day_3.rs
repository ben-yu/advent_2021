pub fn day_3_1() {
    let input = include_str!("../inputs/day_3_1_input.txt");

    let max_size = 12;
    let mut gamma = 0usize;

    let numbers = input.lines()
        .map(|x| usize::from_str_radix(&x, 2).unwrap() ) //convert to int
        .collect::<Vec<usize>>();

    let num_count = numbers.len();

    // bit 0 is on the right, so iterate in reverse
    for idx in (0..max_size).rev() {
        // count 1's for gammma first
        // Shift a 1 by idx to count that position, then sum the count
        let count = numbers.iter().filter(|&n| (n & (1 << idx)) > 0).count();

        if count > num_count / 2 {
            gamma += 1 << idx;
        }
    }

    println!("Gamma {}", gamma);
    // Epsilon is complement
    let epsilon = !gamma & 0b11111111111;
    println!("Epsilon {}", epsilon);
    println!("Day 3 {}", gamma * epsilon)
}
