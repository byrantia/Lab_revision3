import employee_info as info

def test_age():
    result = [
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]

    test = info.get_employees_by_age_range(20,26)

    assert test == result

def test_avg():
    result = 60166.67
    test = info.calculate_average_salary()
    assert test == result

def test_dept():
    result = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},]
    test = info.get_employees_by_dept("Marketing")
    assert test == result