from app import schemas
from .database import client, session

def test_root(client):
    res = client.get('/')
    # print(res)
    print(res.json().get('message'))
    assert res.json().get('message') == 'welcome to api'
    assert res.status_code == 200

def test_user_create(client):
    res = client.post('/users/', json={"email": "tushar3549@gmail.com", "password": "tushar1234"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "tushar3549@gmail.com"
    # print(res.json())
    assert res.status_code == 201
