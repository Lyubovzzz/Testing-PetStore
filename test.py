import json
import requests

# GET
status = "available"

res=requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())

# POST
data = json.dumps({
  "id": 0,
  "category": {
    "id": 0,
    "name": "Jack"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Jack"
    }
  ],
  "status": "available"
})
headers = {'accept': 'application/json', "Content-Type" : "application/json"}
res = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, data = data)
print(res.status_code)
print(res.json())


# PUT
data = json.dumps({
  "id": 0,
  "category": {
    "id": 0,
    "name": "Monika"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Monika"
    }
  ],
  "status": "sold"
})
headers = {'accept': 'application/json', "Content-Type" : "application/json"}
res = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, data = data)
print(res.status_code)
my_dict = dict(res.json())
pet_id = my_dict.get('id')

# DELETE
res = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}')
print(res.status_code)
print(res.json())

