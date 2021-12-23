use regex::Regex;
use std::cmp::{max, min};
use std::collections::HashSet;
use immense::*;
use rand::thread_rng;
use rand::seq::SliceRandom;
use std::fs::File;


fn line_intersect(x0: i64, x1: i64, ox0: i64, ox1: i64) -> bool {
    (x0 <= ox0 && ox0 <= x1)
        || (x0 <= ox1 && ox1 <= x1)
        || (ox0 <= x0 && x0 <= ox1)
        || (ox0 <= x1 && x1 <= ox1)
}

fn get_line_intersect(p0: i64, p1: i64, op0: i64, op1: i64) -> (i64, i64) {
    let r0 = if op0 < p0 { p0 } else { op0 };
    let r1 = if op1 < p1 { op1 } else { p1 };

    (r0, r1)
}

struct Cuboid {
    x0: i64,
    x1: i64,
    y0: i64,
    y1: i64,
    z0: i64,
    z1: i64,
    overlaps: Vec<Cuboid>,
}

impl Cuboid {
    fn new(x0 : i64, x1: i64, y0: i64, y1: i64, z0: i64, z1: i64) -> Cuboid {
        Cuboid {
            x0: x0,
            x1: x1,
            y0: y0,
            y1: y1,
            z0: z0,
            z1: z1,
            overlaps: Vec::new(),
        }
    }

    fn intersects(&self, cube: &Cuboid) -> bool {
        line_intersect(self.x0, self.x1, cube.x0, cube.x1) &&
            line_intersect(self.y0, self.y1, cube.y0, cube.y1) &&
            line_intersect(self.z0, self.z1, cube.z0, cube.z1)
    }

    fn subtract(&mut self, cube: &Cuboid) {
        if self.intersects(cube) {
            let x = get_line_intersect(self.x0, self.x1, cube.x0, cube.x1);
            let y = get_line_intersect(self.y0, self.y1, cube.y0, cube.y1);
            let z = get_line_intersect(self.z0, self.z1, cube.z0, cube.z1);

            self.overlaps.iter_mut().for_each(|x| x.subtract(cube));
            self.overlaps.push(Cuboid::new(x.0, x.1, y.0, y.1, z.0, z.1));

        }
    }

    fn volume(&self) -> u128 {
        ((self.x1 - self.x0 + 1) as u128
            * (self.y1 - self.y0 + 1) as u128
            * (self.z1 - self.z0 + 1) as u128)
            - self.overlaps.iter().map(|x| x.volume()).sum::<u128>()
    }
}

impl ToRule for Cuboid {
    fn to_rule(&self) -> Rule {
        let mv: Tf = Tf::t(self.x0 as f32, self.y0 as f32, self.z0 as f32);
        let scale: Tf = Tf::sby((self.x1-self.x0) as f32, (self.y1-self.y0) as f32, (self.z1-self.z0) as f32);
        let mut rng = thread_rng();
        let choices = [
            // Red
            Tf::color(Hsv::new(0.0, 1.0, 1.0)),
            // Black
            Tf::color(Hsv::new(120.0, 1.0, 1.0)),
        ];
        let color: Tf = *choices.choose(&mut rng).unwrap();
        rule![
            tf![mv, scale, color] => cube(),
        ]
    }
}

pub fn day_22_1() {
    let re = Regex::new(r"x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)").unwrap();
    let mut pts: HashSet<(i64, i64, i64)> = HashSet::new();

    let mut cuboids: Vec<Cuboid> = Vec::new();
    for l in include_str!("../inputs/day_22_input.txt").split("\n") {

        let t: Vec<_> = re
            .captures(l)
            .unwrap()
            .iter()
            .skip(1)
            .map(|x| x.unwrap().as_str().parse::<i64>().unwrap())
            .collect();
        println!("{:?}", t);
        if t[0] > 50 || t[1] < -50 || t[2] > 50 || t[3] < -50 || t[4] > 50 || t[5] < -50 {
            continue;
        }

        for x in max(t[0], -50)..min(50, t[1] + 1) {
            for y in max(t[2], -50)..min(50, t[3] + 1) {
                for z in max(t[4], -50)..min(50, t[5] + 1) {
                    if l.contains("on") {
                        pts.insert((x, y, z));
                    } else {
                        pts.remove(&(x, y, z));
                    }
                }
            }
        }
    }
    println!("Part 1: {}", pts.len());
}

pub fn day_22_2() {
    let re = Regex::new(r"x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)").unwrap();

    let mut cuboids: Vec<Cuboid> = Vec::new();
    for l in include_str!("../inputs/day_22_input.txt").split("\n") {

        let t: Vec<_> = re
            .captures(l)
            .unwrap()
            .iter()
            .skip(1)
            .map(|x| x.unwrap().as_str().parse::<i64>().unwrap())
            .collect();
        let new_c = Cuboid::new(t[0], t[1], t[2], t[3], t[4], t[5]);
        cuboids.iter_mut().for_each(|x| x.subtract(&new_c));
        if l.contains("on") {
            cuboids.push(new_c);
        }
    }
    let s = cuboids.iter().map(|x| x.volume() as u128).sum::<u128>();

    println!("Part 2: {}", s);
    let colors_filename = String::from("colors.mtl");
    let mut output_file = File::create("mesh.obj").unwrap();
    write_meshes(ExportConfig {
                        export_colors: Some(colors_filename),
                        ..ExportConfig::default()
                    },
                 cuboids.iter()
                    .flat_map(|x| x.to_rule().generate()),
                 &mut output_file);
}
