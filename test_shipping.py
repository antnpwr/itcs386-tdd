import pytest
from shipping import shipping_fee

def test_weight_must_be_more_than_0kg():
    with pytest.raises(ValueError):
        shipping_fee(0)

@pytest.mark.parametrize("weight, expected", [
    (0.1, 40), # up to 1 kg
    (0.5, 40), # up to 1 kg
    (1, 40), # up to 1 kg
    (1.1, 60), # more than 1 kg up to 5 kg
    (2.5, 60), # more than 1 kg up to 5 kg
    (5, 60), # more than 1 kg up to 5 kg
    (5.2, 70), # more than 5 kg 
    (6, 70), # more than 5 kg
    (7.5, 90), # more than 5 kg
    (10, 110), # more than 5 kg
])

def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected

