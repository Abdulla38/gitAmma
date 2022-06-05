from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token="5455820081:AAFPpzfdvkNZ0SJfv24zt8WHC9uPmhT_RWo")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-RU")

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + "\n"
    resp_msg += f"Текущая температура: {celsius}°C\n"
    resp_msg += f"Погода на улице: {weather.current.sky_text}\n"

    if celsius < 10:
        resp_msg += "\nПрохладно, оденься по теплее"
    else:
         resp_msg += "\nТепло, оденься по легчее"

    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)