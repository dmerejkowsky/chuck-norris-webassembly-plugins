use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn get_fact() -> String {
    "Chuck Norris can slam a revolving door".to_string()
}

#[wasm_bindgen]
pub fn answer() -> i32 {
    42
}
