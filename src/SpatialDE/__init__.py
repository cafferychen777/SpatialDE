from importlib.metadata import PackageNotFoundError, version

from .base import dyn_de
from .base import run
from .base import model_search
from .aeh import fit_patterns
from .aeh import spatial_patterns

try:
    __version__ = version("spatialde-modern")
except PackageNotFoundError:
    __version__ = "1.1.3.post1"
