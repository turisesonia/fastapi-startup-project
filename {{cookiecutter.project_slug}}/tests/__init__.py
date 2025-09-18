import pytest

skip_by_default = pytest.mark.skipif(
    "not config.getoption('--not-skip')",
    reason="Skipping unless --not-skip is provided",
)
