import pytest
@pytest.mark.smoke
def test_get_user(api):
    response = api.get("users/1")

    assert response.status_code == 200

    data = response.json()

    assert data, "Response is empty"
    assert isinstance(data, dict)

    assert data["id"] == 1
    assert isinstance(data["name"], str)

    assert isinstance(data["email"], str)
    assert "@" in data["email"]

def test_get_nonexistent_user(api):
    response = api.get("users/99999")

    assert response.status_code in [404, 400]

def test_get_negative_id_user(api):
    response = api.get("users/-1")

    assert response.status_code in [404, 400]

