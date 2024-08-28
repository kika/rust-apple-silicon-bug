mod bug;
use bug::Builder;

pub fn main() {
  let app: Builder = Builder::builder();
  println!("# of endpoints {}", app.trouble());
}
