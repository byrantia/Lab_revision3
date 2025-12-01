import price_info as price

def test_total():
    result = 46.75
    test = price.total_cost_shopping()
    assert test == result

def test_cost_of_fruit():
    result = 6.5
    test = price.cost_of_fruits('watermelon',1)
    assert test == result