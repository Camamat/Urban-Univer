from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/user/admin")
async def admin() -> dict:
    return {'message' : 'Вы вошли как администратор'}

@app.get("/user/{user_id}")
async def user(user_id : int) -> dict:
    return {'message' : f'Вы вошли как пользователь № {user_id}'}

@app.get("/user/{username}/{age}")
async def user_new(username : str = Path(min_length=5, max_length=20, description='Enter username',
                                         example='UrbanUser'), age : int = Path(ge=18, le=120, description='Enter age',
                                                                                example='24')) -> dict:
    return {'User' : username, 'Age' : age}

@app.get("/user/{user_id}")
async def user_id(user_id : int = Path(ge=1, le=100, description='Enter User ID', example='5')) -> dict:
    return {'User' : user_id}

@app.get("/")
async def welcome() -> dict:
    return {'message' : 'Главная страница'}