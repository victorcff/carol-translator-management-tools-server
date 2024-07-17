from sqlalchemy.orm import Session
from app.models.payments import Payment
from app.models.events import Event

class EventRepository:
    @staticmethod
    def find_all(db: Session) -> list[Payment]:
        return db.query(Payment).all()

    @staticmethod
    def save(db: Session, payment: Payment) -> Payment:
        if payment.id:
            db.merge(payment)
        else:
            db.add(payment)
        db.commit()
        return payment

    @staticmethod
    def find_by_id(db: Session, id: int) -> Payment:
        return db.query(Payment).filter(Payment.id == id).first()
    
    @staticmethod
    def find_by_event(db: Session, id: int) -> Payment:
        event = db.query(Event).filter(Event.id == id).first()
        return db.query(Payment).filter(Payment.id == event.payment_id)

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Payment).filter(Payment.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        payment = db.query(Payment).filter(Payment.id == id).first()
        if payment is not None:
            db.delete(payment)
            db.commit()
