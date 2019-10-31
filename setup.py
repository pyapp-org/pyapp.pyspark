from pathlib import Path
from setuptools import setup

here = Path(__file__).parent

about = {}
with (here / "pyapp_ext/pyspark/__version__.py") as f:
    exec(f.read_text(), about)

setup(version=about["__version__"])
