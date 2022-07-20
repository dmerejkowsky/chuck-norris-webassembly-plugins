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
    assert output.exists()
    yield output


@pytest.fixture(scope="session")
def assembly_script_wasm():
    cmd = ["npm", "run", "asbuild:debug"]
    print(cmd)
    subprocess.run(cmd, cwd=Path("assembly-script"))
    this_path = Path.cwd()
    output = this_path / "assembly-script/build/debug.wasm"
    assert output.exists()
    yield output


def test_rust(rust_wasm):
    store = Store(engine.Universal(Compiler))
    module = Module(store, rust_wasm.read_bytes())
    instance = Instance(module)
    actual = instance.exports.answer()
    assert actual == 42


def test_assembly_script(assembly_script_wasm):
    store = Store(engine.Universal(Compiler))
    module = Module(store, assembly_script_wasm.read_bytes())
    instance = Instance(module)
    actual = instance.exports.answer()
    assert actual == 42
