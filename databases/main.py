from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Integer, create_engine
from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


connection_string = f"sqlite:///{BASE_DIR}/test.db"

Base = declarative_base()
engine = create_engine(connection_string, echo=True)


Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.utcnow)


def __repr__(self):
    return f"<User {self.username} email={self.email}>"

