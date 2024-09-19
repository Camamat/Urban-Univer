from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *



api = ''
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard= True)
button = KeyboardButton( text= 'Рассчитать')
button_2 = KeyboardButton( text= 'Информация')
button_3 = KeyboardButton( text= 'Купить')
kb.add(button)
kb.add(button_2)
kb.add(button_3)

keyboard = InlineKeyboardMarkup()
but_1 = InlineKeyboardButton(text= 'Product1', callback_data= 'product_buying')
but_2 = InlineKeyboardButton(text= 'Product2', callback_data= 'product_buying')
but_3 = InlineKeyboardButton(text= 'Product3', callback_data= 'product_buying')
but_4 = InlineKeyboardButton(text= 'Product4', callback_data= 'product_buying')
keyboard.add(but_1)
keyboard.add(but_2)
keyboard.add(but_3)
keyboard.add(but_4)
@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup= keyboard)

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    products = get_all_products()
    i = 0
    for product in products:
        i = i + 1
        with open(f'{i}.png', 'rb') as img:
            await message.answer_photo(img, f'Название:{product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    await message.answer('Выберите продукт для покупки:', reply_markup= keyboard)

@dp.callback_query_handler(text= 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.callback_query_handler(text= 'formulas')
async def infor(call):
    await call.message.answer('Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup= kb)
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age= message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth= message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f"Ваша норма калорий {calories}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)