from main import User, Session, engine

local_session = Session(bind=engine)

users = [
    {'username': 'johndoe4', 'email': 'jondoe13@helo.com'},
    {'username': 'janedoe5', 'email': 'jondoe13@hello.com'},
]    


# new_user = User(username='johndoe2', email="hello2@hello.com")
# local_session.add(new_user)
# local_session.commit()

for user in users:
    new_user = User(username=user['username'], email=user['email'])
    local_session.add(new_user)
    local_session.commit()
    print(f"Added user {new_user.username}")