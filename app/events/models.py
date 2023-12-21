from sqlalchemy import Column, Integer, String, DateTime
from app.event.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    attendees = Column(String)
    event_id = Column(String, unique=True, index=True, nullable=False)
    category = Column(String, nullable=False)
    status = Column(String, nullable=False)
    location = Column(String, nullable=False)
    address = Column(String, nullable=False)

class Queue(Base):
    __tablename__ = "queues"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    position = Column(Integer, nullable=False)
    status = Column(String, nullable=False)

    user = relationship("users", backref="queues")
    event = relationship("events", backref="queues")