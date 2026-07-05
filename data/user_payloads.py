CREATE_USER_PAYLOAD = {
    "name": "Anna",
    "email": "anna@test.com"
}

UPDATE_USER_PAYLOAD = {
    "id": 1,
    "name": "Kate",
    "email": "kate@test.com"
}

INVALID_CREATE_USER_PAYLOADS = [
    {
        "name": "",
        "email": "ab@cd.ru"
    },
    {
        "name": "     ",
        "email": "ab@cd.ru"
    },
    {
        "name": 123,
        "email": "ab@cd.ru"
    },
    {
        "name": "Anna"
    },
    {
        "name": "Anna",
        "email": "abcd"
    },
    {
        "name": "Anna",
        "email": "ab@cd.ru",
        "super_flag": 1
    }
]

INVALID_UPDATE_USER_PAYLOADS = [
    {
        "id": 1,
        "name": "",
        "email": "test@test.com"
    },
    {
        "id": 1,
        "name": "     ",
        "email": "test@test.com"
    },
    {
        "id": 1,
        "name": 123,
        "email": "test@test.com"
    },
    {
        "name": "Anna",
        "email": "test@test.com"
    },
    {
        "id": 1,
        "name": "Anna",
        "email": "abcd"
    },
    {
        "id": 1,
        "name": "Anna",
        "email": "ab@cd.ru",
        "super_flag": 1
    }
]