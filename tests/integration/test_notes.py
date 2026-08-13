from pages.notes_page import NotesPage
from playwright.sync_api import expect
from data.factories.note_factory import NoteFactory

def test_notes_page_open(notes):
    expect(notes.add_note_button).to_be_visible()
    
def test_create_note(notes, notes_client):
    created_data = NoteFactory.create()

    notes.create_note(created_data)

    created_note = notes_client.get_notes()[0]

    card = notes.get_note_by_id(created_note["id"])

    assert card.get_title() == created_data.title
    assert card.get_description() == created_data.description
    assert not card.is_completed()
        
def test_edit_note(notes, notes_client):
    created_data = NoteFactory.create(
        completed = True
    )

    notes.create_note(created_data)

    note_id = notes_client.get_notes()[0]["id"]

    created_card = notes.get_note_by_id(note_id)

    assert created_card.get_title() == created_data.title
    assert created_card.get_description() == created_data.description
    assert created_card.is_completed()

    modal = created_card.edit()

    update_data = NoteFactory.create(
        category="Personal",
        title="edited note",
        description="description edited note",
    )

    modal.fill_form(update_data)
    modal.submit()

    notes.wait_notes_loaded()

    edited_card = notes.get_note_by_id(note_id)

    assert edited_card.get_title() == update_data.title
    assert edited_card.get_description() == update_data.description
    assert not edited_card.is_completed()

def test_delete_note(notes, notes_client):
    modal = notes.open_create_form()

    create_data = NoteFactory.create()

    modal.fill_form(create_data)
    modal.submit()

    notes.wait_notes_loaded()

    note_id = notes_client.get_notes()[0]["id"]

    card = notes.get_note_by_id(note_id)

    modal = card.delete()
    modal.delete()

    response = notes_client.get_note(note_id)
    assert response.status_code == 404

def test_completed_note(notes, notes_client):
    created_data = NoteFactory.create()

    notes.create_note(created_data)

    note_id = notes_client.get_notes()[0]["id"]

    created_card = notes.get_note_by_id(note_id)

    assert not created_card.is_completed()

    # old_progress = notes.get_completed_count()

    response = notes_client.completed_note(
        note_id,
        {
            "completed": True
        }
        )

    assert response.status_code == 200
    assert response.json()["data"]["completed"] is True

    notes.reload()

    cards = notes.get_notes()

    first_completed = next(
        card
        for card in cards
        if card.is_completed()
    )

    completed_card = notes.get_note_by_id(note_id)

    # new_progress = notes.get_completed_count()

    assert completed_card.is_completed()
    assert completed_card.get_title_background_color() == "rgba(40, 46, 41, 0.6)"
    assert first_completed.get_id() == note_id
    # assert new_progress == old_progress + 1













