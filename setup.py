from setuptools import setup, Extension
import sys
from pathlib import Path

base = Path(__file__).parent / "flexhash"

def glob_src(subdir):
    p = base / subdir
    return [str(x) for x in p.rglob("*.c")] if p.exists() else []

extra_compile_args = ["/O2"] if sys.platform == "win32" else ["-O3", "-fvisibility=hidden"]

ext = Extension(
    "flexhash._flexhash",
    sources=[str(base / "_flexmodule.c"), str(base / "flex.c")] + glob_src("sha3") + glob_src("cryptonote"),
    include_dirs=[str(base), str(base / "sha3"), str(base / "cryptonote")],
    extra_compile_args=extra_compile_args,
)

setup(
    name="flexhash",
    version="0.1.0",
    description="Kylacoin Flex hashing (C extension)",
    packages=["flexhash"],
    ext_modules=[ext],
    python_requires=">=3.8",
)
