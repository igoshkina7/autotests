def test_register(auth_client, test_user):
    response = auth_client.register(**test_user)
    
    assert response.status_code == 201 

def test_login(auth_client, test_user):
    token = auth_client.login(
        test_user["email"],
        test_user["password"]
    )

    print(auth_client.session.headers)

    assert token