from itertools import chain

struct_size = 621

struct_preamble = "pub struct Builder {"

impl_preamble = """
impl Builder {
    pub fn trouble(self) -> usize
    {
        let endpoints = ["""

service_preamble = """
impl Builder {
    pub fn builder() -> Builder {
        Builder {
"""

def generate(length):
    struct_lines = []
    impl_lines = []
    service_lines = []
    

    for counter in range(length):
        handler_name = f'handler_{counter}'
        struct_lines.append(f'    {handler_name}: Option<String>,')
        impl_lines.append(f'    self.{handler_name}.unwrap(),')
        service_lines.append(f'{handler_name}: None,')
    
    return '\n'.join(
        chain(
            [struct_preamble],
            struct_lines,
            ["}"],
            [impl_preamble],
            impl_lines,
            [" ]; endpoints.len() } }"],
            [service_preamble],
            service_lines,
            ["}}}"] 
        ))

if __name__ == "__main__":
    rust = generate(struct_size)
    print(rust)
