use sqlx::{self, Connection};
use tokio;
use rand::{prelude::*,distributions::Alphanumeric, Rng};
use argon2::{password_hash::PasswordHasher,Argon2};

#[tokio::main]
async fn main() {
    let mut conn = sqlx::SqliteConnection::connect("/etc/vote/vote.db").await.unwrap();
    let salt = "mDUIuDJzLud1affbdtGjWw"; //predetermined salt
    let argon2 = Argon2::default();
    for _ in 0..1024{
    let mut rng = thread_rng();
    let user = rng.next_u32();
    let password: String = rng.sample_iter(&Alphanumeric).take(12).map(char::from).collect();
    println!("{}:{}",user,password);
    let p = argon2.hash_password(password.as_bytes(), &salt).unwrap().to_string();
    sqlx::query("INSERT INTO Voters (ssn,password) VALUES (?,?)").bind(user).bind(p).execute(& mut conn).await.unwrap();
    }
}
