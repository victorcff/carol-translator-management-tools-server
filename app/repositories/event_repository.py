from sqlalchemy.orm import Session
from app.models.events import Event

class EventRepository:
    @staticmethod
    def find_all(db: Session) -> list[Event]:
        return db.query(Event).all()

    @staticmethod
    def save(db: Session, event: Event) -> Event:
        if event.id:
            db.merge(event)
        else:
            db.add(event)
        db.commit()
        return event

    @staticmethod
    def find_by_id(db: Session, id: int) -> Event:
        return db.query(Event).filter(Event.id == id).first()
    
    @staticmethod
    def find_by_name(db: Session, name: str) -> Event:
        return db.query(Event).filter(Event.name == name).all()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Event).filter(Event.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        event = db.query(Event).filter(Event.id == id).first()
        if event is not None:
            db.delete(event)
            db.commit()
