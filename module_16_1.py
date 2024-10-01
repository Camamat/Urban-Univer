from fastapi import FastAPI

app = FastAPI()

@app.get("/user/admin")
async def admin() -> dict:
    return {'message' : 'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user(user_id : int) -> dict:
    return {'message' : f'Вы вошли как пользователь № {user_id}'}

@app.get("/user")
async def user_id(username : str, age : int) -> dict:
    return {'User' : username, 'Age' : age}

@app.get("/")
async def welcome() -> dict:
    return {'message' : 'Главная страница'}
