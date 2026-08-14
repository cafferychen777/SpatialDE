# SpatialDE Modern

`spatialde-modern` is a maintained fork of
[SpatialDE](https://github.com/Teichlab/SpatialDE), a method for identifying
genes whose expression depends on spatial or temporal coordinates.

The distribution keeps the original `SpatialDE` import package and numerical
API while supporting current Python, NumPy, pandas, and SciPy releases. It is
published under a distinct distribution name so it cannot be confused with an
official release from the original authors.

## Installation

```bash
pip install spatialde-modern
```

The import name remains unchanged:

```python
import SpatialDE
```

## Minimal example

```python
import pandas as pd
import SpatialDE

coordinates = pd.DataFrame({"x": [0, 0, 1, 1], "y": [0, 1, 0, 1]})
expression = pd.DataFrame(
    {
        "gene_a": [0.1, 0.2, 1.1, 1.2],
        "gene_b": [0.5, 0.4, 0.6, 0.5],
    }
)

results = SpatialDE.run(coordinates, expression)
```

## Maintenance scope

This repository contains only the maintained Python distribution. The original
paper analyses, datasets, notebooks, R implementation, and historical Stan
experiments remain available in the
[upstream repository](https://github.com/Teichlab/SpatialDE). They are not
runtime dependencies and are intentionally excluded here.

Compatibility fixes in this fork include:

- replacement of the removed `scipy.misc.derivative` API;
- conversion of removed top-level SciPy array aliases to NumPy;
- support for current pandas array semantics;
- built-in `stabilize` and `regress_out` preprocessing, replacing the separate
  NaiveDE runtime dependency used by the original command-line workflow;
- modern PEP 517/621 packaging with complete runtime dependencies;
- isolated wheel builds and real numerical smoke tests in CI.

## Attribution and license

SpatialDE was created by Valentine Svensson and collaborators. This maintained
fork preserves the original MIT license and records its upstream base in
[`NOTICE.md`](NOTICE.md).
