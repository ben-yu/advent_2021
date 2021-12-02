use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn day_1_1() {
    let mut depths = Vec::new();
    if let Ok(lines) = read_lines("./inputs/day_1_1_input.txt") {
        for line in lines {
            if let Ok(depth) = line {
                depths.push(depth.parse::<u32>().unwrap());
            }
        }
    }

    let mut count = 0;
    let mut a = depths[0];

    for i in depths {
        if i > a {
            count = count + 1
        }
        a = i
    }
    println!("Day 1 Answer: {}", count);
}

pub fn day_1_2() {
    let mut depths = Vec::new();
    if let Ok(lines) = read_lines("./inputs/day_1_1_input.txt") {
        for line in lines {
            if let Ok(depth) = line {
                depths.push(depth.parse::<u32>().unwrap());
            }
        }
    }

    let mut count = 0;
    let mut cur_sum;
    let mut prev_sum = 0;

    let mut a = depths[0];
    let mut b = depths[1];

    for d in &depths[2..] {
        let c = *d;
        cur_sum = a + b + c;
        if cur_sum > prev_sum {
            count = count + 1;
        }
        a = b;
        b = c;
        prev_sum = cur_sum;
    }
    println!("Day 1 Answer: {}", count-1);
}
