from importlib.metadata import PackageNotFoundError, version

from .aeh import fit_patterns, spatial_patterns
from .base import dyn_de, model_search, run
from .preprocessing import regress_out, stabilize

try:
    __version__ = version("spatialde-modern")
except PackageNotFoundError:
    __version__ = "1.1.3.post2"

__all__ = [
    "dyn_de",
    "fit_patterns",
    "model_search",
    "regress_out",
    "run",
    "spatial_patterns",
    "stabilize",
]
