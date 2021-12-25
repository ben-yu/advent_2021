use std::cmp::{max, min};
use std::collections::HashMap;

pub fn day_21_1() {
    let mut one_pos = 10;
    let mut two_pos = 7;

    let mut dice_roll = 1;
    let mut one_score = 0;
    let mut two_score = 0;
    let mut turn = 0;

    while one_score < 1000 && two_score < 1000 {
        if turn % 2 == 0 {
            let mut one_move = 0;
            for i in 1..4 {
                one_move += dice_roll;
                dice_roll += 1;
                if dice_roll > 100 {
                    dice_roll = 1;
                }
            }
            one_pos += one_move;
            if one_pos > 10 {
                one_pos = one_pos % 10;
                if one_pos == 0 {
                    one_pos = 10;
                }
            }
            one_score += one_pos;
            println!("Player 1 rolls {} and moves to space {} for a total score of {}", one_move, one_pos, one_score);
        } else {
            let mut two_move = 0;
            for i in 1..4 {
                two_move += dice_roll;
                dice_roll += 1;
                if dice_roll > 100 {
                    dice_roll = 1;
                }
            }
            two_pos += two_move;
            if two_pos > 10 {
                two_pos = two_pos % 10;
                if two_pos == 0 {
                    two_pos = 10;
                }
            }
            two_score += two_pos;
            println!("Player 2 rolls {} and moves to space {} for a total score of {}",two_move, two_pos, two_score);
        }
        turn += 1;
    }

    println!("Turn {}, Min Score {}", turn, min(one_score,two_score));
    println!("Answer: {}", turn * 3 * min(one_score,two_score));
}

#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
struct Player {
    pos: u64,
    score: u64,
}

impl Player {
    fn new(pos: u64) -> Self {
        Self {
            pos: pos,
            score: 0,
        }
    }

    fn step(&mut self, roll: u64) {
        self.pos = self.pos + roll;
        if self.pos > 10 {
            self.pos = self.pos % 10;
            if self.pos == 0 {
                self.pos = 10;
            }
        }

        self.score += self.position();
    }

    fn position(&self) -> u64 {
        return self.pos;
    }
}

#[derive(Copy, Clone, Eq, PartialEq, Hash, Debug)]
struct Game {
    players: [Player; 2],
}

impl Game {
    fn turn(&self, player: usize, roll: u64) -> Self {
        let mut next = *self;
        next.players[player].step(roll);
        next
    }
}

pub fn day_21_2() {
    let mut one_pos = 10;
    let mut two_pos = 7;

    let mut wins = [0, 0];
    let mut games = HashMap::from([(Game { players: [Player::new(one_pos), Player::new(two_pos)] }, 1u64)]);

    // Rolls are now randomly from 1-3
    // So we generate all possible combinations of the 3 rolls
    let rolls: Vec<_> = (1..4)
        .flat_map(|a| (1..4).flat_map(move |b| (1..4).map(move |c| a + b + c)))
        .collect();

    // Loop until all games end
    for player in (0..2).cycle() {
        let mut next = HashMap::new();
        for &roll in rolls.iter() {
            for (game, universes) in games.iter() {
                let next_turn = game.turn(player, roll);
                if next_turn.players[player].score >= 21 {
                    wins[player] += universes;
                } else {
                    // No winner so add to next iteration
                    *next.entry(next_turn).or_default() += universes
                }
            }
        }
        games = next;
        if games.is_empty() {
            break;
        }
    }

    let [p1_wins, p2_wins] = wins;
    println!("Answer {}", max(p1_wins, p2_wins))
}
