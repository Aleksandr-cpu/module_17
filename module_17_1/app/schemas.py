from pydantic import BaseModel

class UserBase(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateUser (UserBase):
    username: str

class UpdateUser (UserBase):
    pass

class TaskBase(BaseModel):
    title: str
    content: str
    priority: int

class CreateTask(TaskBase):
    pass

class UpdateTask(TaskBase):
    pass
