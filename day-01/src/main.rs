use std::{env, fs, path, process};


fn main() {
    let input_arg = env::args().nth(1); //.expect("Error: Please provide input file path as an argument!");

    let input_str = input_arg.unwrap_or_else(|| {
        eprintln!("Error: Please provide input file path as an argument!");
        process::exit(1);
    });

    let input_path = path::Path::new(&input_str);

    if input_path.exists() && input_path.is_file() {
        println!("Using input file: {}", input_path.to_str().unwrap());
    } else {
        eprintln!("Error: Invalid input file path {}", input_path.to_str().unwrap());
        process::exit(1);
    }

    let data = fs::read_to_string(input_path).unwrap();
    let data_split: Vec<&str> = data.trim().split("\n").collect();
    let mut totals: Vec<u32> = vec![0];

    for entry in data_split.iter() {
        let value = entry.trim().parse::<u32>();

        if value.is_err() {
            totals.push(0);
            continue;
        }

        if let Some(last) = totals.last_mut() {
            *last += value.unwrap();
        }
    }
    totals.sort();

    let max = totals.last().unwrap(); //totals.iter().max().unwrap();
    let top_3_sum: u32 = totals.iter().rev().take(3).sum();

    println!("Max cal: {max}");


    println!("Top 3 cal sum: {top_3_sum}");

}
