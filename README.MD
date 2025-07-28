To setup project:
```
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

To run webservice
```
uvicorn app.main:app --reload
```

To run tests
```
pytest
```

API examples:
- localhost:8000/api/users/1
returns
```
{
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
}
```

- localhost:8000/api/users/
with body
```
{
    "name": "test",
    "email": "test@test.te2st"
}
```

To check formatting:
```flake8 .```