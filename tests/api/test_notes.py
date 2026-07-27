from data.users import TEST_USER
from data.notes import NOTE

def test_create_note(auth_client, notes_client):

    auth_client.login(
        TEST_USER["email"],
        TEST_USER["password"]
    )

    response = notes_client.create_note(NOTE)

    assert response.status_code == 200

    note_id = response.json()["data"]["id"]

    get_response = notes_client.get_note(note_id)

    assert get_response.status_code == 200

def test_update_note(auth_client, notes_client):
    auth_client.login(
        TEST_USER["email"],
        TEST_USER["password"]
    )

    note_data = {
        "title": "aaaaaaaaa",
        "description": "description aaaaaa",
        "completed": False,
        "category": "Home"
    }

    #get_response = notes_client.get_notes()

    #assert get_response.status_code == 200

    notes = notes_client.get_notes()

    assert notes
    
    note_id = notes[0]["id"]

    put_response = notes_client.update_note(note_id, note_data)

    assert put_response.status_code == 200

    body_update_note = put_response.json()

    assert body_update_note["data"]["title"] == note_data["title"]
    assert body_update_note["data"]["description"] == note_data["description"]
    assert body_update_note["data"]["category"] == note_data["category"]

def test_delete_note(auth_client, notes_client):
    auth_client.login(
        TEST_USER["email"],
        TEST_USER["password"]
    )

    response = notes_client.create_note(NOTE)

    assert response.status_code == 200

    note_id = response.json()["data"]["id"]

    delete_response = notes_client.delete_note(note_id)

    assert delete_response.status_code == 200

    get_response = notes_client.get_note(note_id)

    assert get_response.status_code == 404






    

