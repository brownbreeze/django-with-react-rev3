import requests

# TOKEN = '4d3a9e615a3f70bcd5c1a8133c077b67cd88f3a6'
JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2Vy"
    "bmFtZSI6InVzZXIyIiwiZXhwIjoxNTgyNDY1ODA5LCJlbWFpbCI6Ii"
    "J9.zCeVRJX71FnOFsYlThENjKYqF3cknJdxcTR4mVuHNx4"
)

headers = {
    'Authorication' : f'Token {JWT_TOKEN}',
}

res = requests.get("http://localhost:8000/post/1", headers=headers)
print(res.json())