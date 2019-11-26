use std::io::{stdin};

fn main() {
    let stdin = stdin();
    let mut text = String::new();
    
    match stdin.read_line(&mut text) {
            Ok(v) => {
                println!("{}", v);
                println!("{}", text);
            },
            Err(error) => println!("El error es: {}", error)
        };

    println!("{}", text);
}