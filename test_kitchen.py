# Test List
# [ ] 200 g x 3 = 600 g
# [ ] multiplying does not modify original
# [ ] same amount and unit are equal
# [ ] 1 oz is not 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz in grams
# [ ] (200 g + 1 oz) x 2

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)

    
# def test_multiplication_by_two():
#     flour = Quantity(200)
#     flour.times(2)
#     assert flour.amount == 400
    
def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    assert flour.times(3) == Quantity(600)
    assert flour.times(2) == Quantity(400)

def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)