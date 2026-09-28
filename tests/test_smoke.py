"""Smoke tests: verify the package and problem/algorithm interfaces import."""

import blaban


def test_package_imports() -> None:
    assert blaban.__version__


def test_subpackages_import() -> None:
    import blaban.algorithms  # noqa: F401
    import blaban.common  # noqa: F401
    import blaban.experiments  # noqa: F401
    import blaban.problems  # noqa: F401
    import blaban.visualization  # noqa: F401
