# Test List
# [ ] 200 g x 3 = 600 g
# [ ] multiplying does not modify original
# [ ] same amount and unit are equal
# [ ] 1 oz is not 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz in grams
# [ ] (200 g + 1 oz) x 2

from kitchen import Quantity, grams, ounces

    
def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)