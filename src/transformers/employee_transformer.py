
from src.models.department import Department


def transform(data: dict) -> dict:
    new_data = dict()
    new_data = {
        'emp_id': data['id'],
        'full_name': f"{data['first_name']} {data['last_name']}",
        'department': Department[data['department']].value
    }

    new_data['adult'] = is_adult(data['age'])

    new_data['tax_percent'] = calc_tax_percent(data['salary'])
    new_data['after_salary'] = calc_salary_after_tax(
        new_data['tax_percent'], data['salary'])

    return new_data


def is_adult(age: int):
    return age >= 18


def calc_tax_percent(salary: int):
    if salary < 10000:
        tax_percent = 0
    elif 10000 <= salary < 20000:
        tax_percent = 10
    elif 20000 <= salary < 30000:
        tax_percent = 20
    elif 30000 <= salary <= 40000:
        tax_percent = 30
    return tax_percent


def calc_salary_after_tax(tax_percent: int, salary: int):

    new_salary = salary-((salary*(tax_percent/100)))

    return new_salary
