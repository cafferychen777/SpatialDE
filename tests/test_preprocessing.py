import numpy as np
import pandas as pd

from SpatialDE import regress_out, stabilize


def test_regress_out_removes_depth_effect_and_preserves_labels() -> None:
    sample_info = pd.DataFrame(
        {"total_counts": [10.0, 20.0, 40.0, 80.0]},
        index=["s1", "s2", "s3", "s4"],
    )
    depth = np.log(sample_info["total_counts"].to_numpy())
    expression = pd.DataFrame(
        [2.0 + 3.0 * depth, 7.0 - 0.5 * depth],
        index=["gene_a", "gene_b"],
        columns=sample_info.index,
    )

    result = regress_out(sample_info, expression, "np.log(total_counts)")

    assert result.index.equals(expression.index)
    assert result.columns.equals(expression.columns)
    np.testing.assert_allclose(result.var(axis=1), 0.0, atol=1e-20)


def test_stabilize_preserves_dataframe_shape_and_finite_values() -> None:
    counts = pd.DataFrame(
        [[1.0, 2.0, 4.0, 8.0], [2.0, 5.0, 11.0, 23.0]],
        index=["gene_a", "gene_b"],
    )

    result = stabilize(counts)

    assert isinstance(result, pd.DataFrame)
    assert result.shape == counts.shape
    assert np.isfinite(result.to_numpy()).all()
