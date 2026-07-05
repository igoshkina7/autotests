import pytest

from data.user_payloads import (
    CREATE_USER_PAYLOAD,
    INVALID_CREATE_USER_PAYLOADS
)

@pytest.mark.smoke
def test_post_user(api):
    response = api.post(
        "/users",
        json=CREATE_USER_PAYLOAD
    )

    assert response.status_code == 201

    data = response.json()

    assert isinstance(data, dict)
    assert data["id"]

    assert data["name"] == CREATE_USER_PAYLOAD["name"]
    assert data["email"] == CREATE_USER_PAYLOAD["email"]


@pytest.mark.parametrize(
    "payload",
    INVALID_CREATE_USER_PAYLOADS,
    ids=[
        "empty_name",
        "spaces_name",
        "invalid_name_type",
        "missing_email",
        "invalid_email",
        "extra_field"
    ]
)
def test_create_user_invalid_payload(api, payload):
    response = api.post(
        "/users",
        json=payload
    )

    assert response.status_code == 422