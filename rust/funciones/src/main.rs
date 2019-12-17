fn main() {
    let r = mi_function(10);
    println!("{}", r);

    let p : i32 = {
        println!("exp");
        100
    };

    println!("{}", p);

    let a : i32 = if p == 100 {
        20
    } else {
        30
    };

    println!("{}", a);

    let mut counter = 0;
    let r = loop {
        counter += 1;

        println!("looping");

        if counter == 10 {
            break counter
        }
    };

    println!("{}", r);
    


}

fn mi_function(v: i32) -> i32 {
    println!("hola");
    v
}