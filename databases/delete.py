from main import User, Session, engine

local_session = Session(bind=engine)

user_to_delete = local_session.query(User).filter(User.username == 'johndoe4').first()

local_session.delete(user_to_delete)

local_session.commit()
print(f"Deleted user {user_to_delete.username}")