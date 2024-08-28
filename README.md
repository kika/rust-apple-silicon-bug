1. On M1 Max 64GB it takes north of 40 minutes to compile this code. M3 Pro: 25 minutes.
2. The culprit is the `Option<String>` type. If you replace it with just `String` (and `None` with `String::from("some unique string")`) it compiles in seconds.
3. `degenerator.py` generates code for `bug.rs` so you can play with number of fields, etc.
