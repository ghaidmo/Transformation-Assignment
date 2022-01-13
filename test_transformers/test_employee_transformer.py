from src.transformers.employee_transformer import calc_salary_after_tax, calc_tax_percent, is_adult


def test_is_adult():
    assert is_adult(17) == False
    assert is_adult(18) == True
    assert is_adult(20) == True


def test_calc_tax_percent():
    assert calc_tax_percent(9999) == 0
    assert calc_tax_percent(10000) == 10
    assert calc_tax_percent(19999) == 10
    assert calc_tax_percent(20000) == 20
    assert calc_tax_percent(29999) == 20
    assert calc_tax_percent(30000) == 30
    assert calc_tax_percent(39999) == 30


def test_calc_salary_after_tax():
    assert calc_salary_after_tax(10, 10000) == 9000
    assert calc_salary_after_tax(20, 20000) == 16000
    assert calc_salary_after_tax(30, 30000) == 21000


def transform():
    data = {"id": "123", "first_name": "Belal", "last_name": "Ali",
            "age": 15, "department": "IT", "salary": 35000}
    new_data = {"emp_id": "123", "full_name": "Belal Ali", "Adult": False,
                "department": "it-services.com", "tax_percent": 30, "after_salary": 24.500}
    assert transform(data) == new_data
    data = {"id": "123", "first_name": "Ghaid", "last_name": "Mousa",
            "age": 23, "department": "IT", "salary": 20000}
    new_data = {"emp_id": "123", "full_name": "Ghaid Mousa", "Adult": True,
                "department": "it-services.com", "tax_percent": 20, "after_salary": 16000}
    assert transform(data) == new_data
