use rocket::tokio::time::{sleep, Duration};

// fn main() {
//     println!("Hello, world!");
// }

#[macro_use]
extern crate rocket;

#[get("/")]
async fn index() -> &'static str {
    "Hello, world!"
}

#[get("/delay/<seconds>")]
async fn delay(seconds: u64) -> String {
    sleep(Duration::from_secs(seconds)).await;
    format!("Waited fro {} seconds", seconds)
}

#[get("/world")]
async fn index_world() -> &'static str {
    "Hello, world!"
}

// #[launch]
// fn rocket() -> _ {
//     rocket::build()
//         .mount("/", routes![index])
//         .mount("/hello", routes![index_world])

// }

#[rocket::main]
async fn main() -> Result<(), rocket::Error> {
    let _rocket = rocket::build()
        .mount("/", routes![index, delay])
        .mount("/hello", routes![index_world])
        .launch()
        .await?;
    Ok(())
}