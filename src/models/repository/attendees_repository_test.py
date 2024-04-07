import pytest
from .attendees_repository import AttedndeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "meu-uuid"
    attendees_info = {
        "uuid": "meu-uuid-attendee",
        "name": "attendee name",
        "email": "email@email.com",
        "event_id": event_id

    }

    attendees_repository = AttedndeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="teste de integração")
def test_get_attendee_badge_by_id():
    attendee_id = "meu-uuid-attendee"
    attendees_repository = AttedndeesRepository()
    attendee = attendees_repository.get_attendee_bedge_by_id(attendee_id)

    print(attendee)
    print(attendee.title)
