import pytest
from app import schemas

def test_root(client):
    res = client.get('/')
    assert res.json().get('message') == 'Welcome to Fast API'


def test_create_user(client):
    res = client.post('/users/', json={"email": 'test@email.com', "password": "password"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test@email.com"
    assert res.status_code == 201

def test_login_user(client):
    res = client.post('/login', data={"username": 'test@email.com', "password": "password"}) # sends the login information as form data
    assert res.status_code == 200


@pytest.mark.parametrize("email, password, status_code",[
    ('wrongemail@gmail.com', 'password123', 403),
    ('sanjeev@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 422),
    ('sanjeev@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        '/login',
        data={
            "username": email,
            "password": password
        }
    )

    assert res.status_code == status_code
    assert  res.json().get('detail') == 'Invalid Credentials'