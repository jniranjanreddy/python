from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str
    age: int
    email: str = Field(...)

# Creating an instance of the Person class
person = Person(name="Alice", age=30, email="alice@example.com")
print(person)