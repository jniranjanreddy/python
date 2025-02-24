from main import User, Session, engine

local_session = Session(bind=engine)

# users = local_session.query(User).all() # query all users
# users = local_session.query(User).all()[:3] # query the first 3 users

users = local_session.query(User).filter(User.username == 'johndoe4').all() # query a user by username
# users = local_session.query(User).filter(User.username == 'johndoe4').first() # query a user by username



for user in users:
    print(user.username, user.email)