from main import User, Base, engine
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
