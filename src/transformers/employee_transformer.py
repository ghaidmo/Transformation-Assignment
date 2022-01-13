from models.department import Department


def transform(data: dict) -> dict:
    new_data = dict()
    new_data = {
        'emp_id': data['id'],
        'full_name': f"{data['first_name']} {data['last_name']}",
        'department': Department[data['department']].value
    }

    new_data['adult'] = data['age'] > 18

    if data['salary'] < 10000:
        tax_percent = 0
    elif 10000 <= data['salary'] < 20000:
        tax_percent = 10
    elif 20000 <= data['salary'] < 30000:
        tax_percent = 20
    elif 30000 <= data['salary'] <= 40000:
        tax_percent = 30

    new_data['tax_percent'] = tax_percent
    new_data['after_salary'] = data['salary']-(data['salary']*tax_percent/100)

    return new_data
