import json

json_str = '''
    {
        "players": [
            {
                "name": "Alex",
                "id": 1,
                "coins": 100
            },
            {
                "name": "Jack",
                "id": 2,
                "coins": 200
            }
        ]
    }
'''

data = json.loads(json_str)
print(data['players'][0])