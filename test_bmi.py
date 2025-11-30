import Lab_2_revision.bmi as bmi

def test_normal_weight():
    result = 0

    test = bmi.calculate_bmi(weight=58,height=1.76)

    assert test == result

def test_over_weight():
    result = 1

    test = bmi.calculate_bmi(weight=590,height=1.76)

    assert test == result

def test_under_weight():
    result = -1

    test = bmi.calculate_bmi(weight=5,height=1.76)

    assert test == result