import pytest
from data.user_payloads import (
    UPDATE_USER_PAYLOAD, 
    INVALID_UPDATE_USER_PAYLOADS
)

@pytest.mark.smoke
def test_put_user(api):  
    response = api.put(
        "/users/1", 
        json=UPDATE_USER_PAYLOAD
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert data["name"] == UPDATE_USER_PAYLOAD["name"]
    assert data["email"] == UPDATE_USER_PAYLOAD["email"]

@pytest.mark.parametrize(
    "payload",
    INVALID_UPDATE_USER_PAYLOADS,
    ids=[
        "empty_name",
        "spaces_name",
        "invalid_name_type",
        "missing_id",
        "invalid_email",
        "extra_field"
    ]
)
def test_update_user_invalid_payload(api,payload):
    response = api.put("/users", json=payload)
    assert response.status_code == 422