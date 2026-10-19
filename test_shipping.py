import pytest
from shipping import shipping_fee

# The weight must be more than 0 kg. Otherwise raise ValueError.
def test_rule_1():
    with pytest.raises(ValueError, match="weight must be more than 0 kg"):
        shipping_fee(0)

# A parcel of up to 1 kg costs 40 baht.
def test_rule_2():
    assert shipping_fee(1) == 40

def test_rule_3():
    assert shipping_fee(5) == 60

# A parcel of more than 5 kg costs 60 baht plus 10 baht for every started kilogram above 5 kg. A 5.2 kg parcel costs 70 baht.
def test_rule_4():
    assert shipping_fee(5.2) == 70