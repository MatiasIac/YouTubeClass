fn main() {
    let r = mi_function(10);
    println!("{}", r);

    let p : i32 = {
        println!("exp");
        100
    };

    println!("{}", p);
}

fn mi_function(v: i32) -> i32 {
    println!("hola");
    v
}