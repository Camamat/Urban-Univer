from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id : int = None
    username : str
    age : int

@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def user_register(user: User, username: str, age: int):
    len_user = len(users)
    if len_user == 0:
        user.id = 1
    else:
        user.id = users[len_user - 1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int, user: str = Body()):
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return edit_user
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    ind_del = 0
    for delete_user in users:
        if delete_user.id == user_id:
            users.pop(ind_del)
            return delete_user
        ind_del += 1
    raise HTTPException(status_code=404, detail='User was not found')