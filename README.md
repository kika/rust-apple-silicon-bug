1. On M1 Max 64GB it takes north of 40 minutes to compile this code. M3 Pro: 25 minutes.
2. The culprit is the `Option<String>` type. If you replace it with just `String` (and `None` with `String::from("some unique string")`) it compiles in seconds.
3. `degenerator.py` generates code for `bug.rs` so you can play with number of fields, etc.

(Issue)[https://github.com/rust-lang/rust/issues/129713]
(Discussion)[https://rust-lang.zulipchat.com/#narrow/channel/247081-t-compiler.2Fperformance/topic/Major.20slowdown.20on.20aarch64-apple-darwin]
(Reddit)[https://www.reddit.com/r/rust/comments/1esagkn/compilation_times_10x_difference_between_m1max/]
