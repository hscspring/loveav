import pytest
from av.config import Config


@pytest.mark.parametrize("dct", [
    {"key1": "val1", "key2": 2}
])
def test_config(dct):
    cg = Config(dct)
    assert cg.key1 == "val1"
    try:
        cg.key_invalid
    except Exception as e:
        assert "invalid" in str(e)
