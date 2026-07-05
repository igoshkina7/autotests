def test_delete_user(api):
    response1 = api.delete("users/1")
    assert response1.status_code in [200, 204]

    data = response1.json()
    assert data["message"] == "User deleted"

    response2 = api.get("users/1")
    assert response2.status_code == 404

def test_delete_invalid_user(api):
    response = api.delete("users/-1")

    assert response.status_code == 404

def test_delete_incorrect_user(api):
    response = api.delete("users/abc")

    assert response.status_code == 404
