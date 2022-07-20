import subprocess
from pathlib import Path

import pytest

from wasmer import engine, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler


@pytest.fixture(scope="session")
def rust_wasm():
    cmd = ["wasm-pack", "build", "--target", "nodejs"]
    print(cmd)
    subprocess.run(cmd, cwd=Path("rust/chuck_norris/"))
    this_path = Path.cwd()
    output = this_path / "rust/chuck_norris/pkg/chuck_norris_bg.wasm"
    yield output


def test_sanity_check(rust_wasm):
    assert rust_wasm.exists()


def test_can_open_wasm_file(rust_wasm):
    store = Store(engine.Universal(Compiler))
    module = Module(store, rust_wasm.read_bytes())
    instance = Instance(module)
    get_fact = instance.exports.get_fact
    actual = get_fact()
    assert "Chuck Norris" in actual
