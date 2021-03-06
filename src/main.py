import json

from src.transformers.employee_transformer import transform

with open('data/input.json') as f:
    lines = f.readlines()

with open("/output.json", "w") as result:
    for line in lines:
        print(line)
        new_data = transform(json.loads(line))
        result.write(json.dumps(new_data) + "\n")
