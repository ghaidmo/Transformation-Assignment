import json
from models import department


def transform(data: dict) -> dict:
    new_data = dict()
    new_data = {'emp_id': data['id'],
                'full_name': data['first_name']+" "+data['last_name']}
    if data['age'] > 18:
        new_data['adult'] = True
    else:
        new_data['adult'] = False

    new_data['department'] = department[data['department']].value

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


f = open('input.json')
lines = f.readlines()
f.close()
result = open("output.json", "w")
for line in lines:
    print(line)
    new_data = transform(json.loads(line))
    result.write(json.dumps(new_data))
result.close()
