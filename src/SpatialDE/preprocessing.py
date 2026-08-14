"""Count preprocessing used by the canonical SpatialDE workflow.

The original SpatialDE command-line and AnnData helpers delegated these two
small operations to NaiveDE. Keeping them next to SpatialDE removes an entire
runtime distribution without changing the numerical workflow.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
import patsy
from scipy import optimize


def regress_out(
    sample_info: pd.DataFrame,
    expression_matrix: pd.DataFrame,
    covariate_formula: str,
    design_formula: str = "1",
    rcond: float | None = -1,
) -> pd.DataFrame:
    """Remove covariate effects while retaining the requested design."""
    covariate_matrix = patsy.dmatrix(f"{covariate_formula} - 1", sample_info)
    design_matrix = patsy.dmatrix(design_formula, sample_info)
    combined_design = np.hstack((design_matrix, covariate_matrix))
    coefficients, *_ = np.linalg.lstsq(
        combined_design,
        expression_matrix.T,
        rcond=rcond,
    )
    covariate_coefficients = coefficients[design_matrix.shape[1] :]
    regressed = expression_matrix - covariate_matrix.dot(covariate_coefficients).T
    return pd.DataFrame(
        regressed,
        index=expression_matrix.index,
        columns=expression_matrix.columns,
    )


def stabilize(expression_matrix: Any) -> Any:
    """Variance-stabilize negative-binomial counts with Anscombe's approximation."""
    means = np.asarray(expression_matrix.mean(axis=1), dtype=float)
    variances = np.asarray(expression_matrix.var(axis=1), dtype=float)
    phi_hat, _ = optimize.curve_fit(
        lambda mean, phi: mean + phi * mean**2,
        means,
        variances,
    )
    return np.log(expression_matrix + 1.0 / (2.0 * phi_hat[0]))


__all__ = ["regress_out", "stabilize"]
