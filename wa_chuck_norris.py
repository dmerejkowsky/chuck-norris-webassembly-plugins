import subprocess
from pathlib import Path

def test_can_generte_rust_wasm():
    subprocess.run(["wasm-pack", "build"], cwd=Path("rust/chuck_norris/")
    this_path = Path(__file__).parent
    assert (this_path / "rust/chuck_norris/pkg/chuck_norris_bg.wasm").exists()


