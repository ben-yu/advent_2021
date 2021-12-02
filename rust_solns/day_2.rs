pub fn day_2_1() {
    let input = include_str!("../inputs/day_2_1_input.txt");

    let mut x = 0;
    let mut y = 0;
    for line in input.lines() {
        let res = line.split(' ').collect::<Vec<&str>>();
        let amt = res[1].parse::<i32>().unwrap();
        match res[0] {
            "forward" => x += amt,
            "up" => y -= amt,
            "down" => y += amt,
            _ => println!("invalid op"),
        }
    }

    println!("Day 2 Answer {}", x*y);
}

pub fn day_2_2() {
    let input = include_str!("../inputs/day_2_1_input.txt");

    let mut x = 0;
    let mut y = 0;
    let mut aim = 0;
    for line in input.lines() {
        let res = line.split(' ').collect::<Vec<&str>>();
        let amt = res[1].parse::<i32>().unwrap();
        match res[0] {
            "forward" => {
                x += amt;
                y += aim * amt;
            }
            "up" => aim -= amt,
            "down" => aim += amt,
            _ => println!("invalid op"),
        }
    }

    println!("Day 2 Answer {}", x*y);
}

