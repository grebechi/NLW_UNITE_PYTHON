from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class AttedndeesRepository:
    def insert_attendee(self, attendees_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                attendee = (
                    Attendees(
                        id = attendees_info.get("uuid"),
                        name = attendees_info.get("name"),
                        email = attendees_info.get("email"),
                        event_id = attendees_info.get("event_id")
                    )
                )
                database.session.add(attendee)
                database.session.commit()

                return attendees_info
            
            except IntegrityError:
                raise Exception('Participante já cadastrado!')
            except Exception as exception:
                database.session.rollback()
                raise exception
                
    def get_attendee_bedge_by_id(self, attendee_id: str) -> Attendees:
        with db_connection_handler as database:
            try:
                attendee = (
                    database.session
                        .query(Attendees)
                        .join(Events, Events.id == Attendees.event_id)
                        .filter(Attendees.id == attendee_id)
                        .with_entities(
                            Attendees.name,
                            Attendees.email,
                            Events.title
                        )
                        .one()
                )
                return attendee
            except NoResultFound:
                return None