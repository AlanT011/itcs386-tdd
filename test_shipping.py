import pytest
from shipping import shipping_fee


@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),
    (1, 40),     # Rule 2: exactly 1 kg
    (1.5, 60),
    (5, 60),
    (5.2, 70),   # Rule 4: round up extra weight
    (6, 70),
    (6.1, 80),   # Rule 4: started extra kg
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 1: zero or negative weight must be rejected
@pytest.mark.parametrize("weight", [0, -1])
def test_invalid_weight(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)