from main import User, Session, engine

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username == 'johndoe1').first()

user_to_update.username = 'niranjan01'

user_to_update.email = 'hello1@hello.com'

local_session.commit()