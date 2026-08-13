from data.users import TEST_USER

def test_register(auth_client):
    response = auth_client.register(**TEST_USER)
    
    assert response.status_code == 201 

def test_login(auth_client):
    token = auth_client.login(
        TEST_USER["email"],
        TEST_USER["password"]
    )

    print(auth_client.session.headers)

    assert token
    
