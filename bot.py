import os
import logging

from aiogram import Bot, Dispatcher, executor, types



SLOVAR = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh',
      'ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'ie','ы':'y','ь':'','э':'e',
      'ю':'iu','я':'ia', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'KH',
      'Ц':'TS','Ч':'CH','Ш':'SH','Щ':'SHCH','Ъ':'IE','Ы':'y','Ь':'','Э':'E',
      'Ю':'IU','Я':'IA',',':'','?':'',' ':' ','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    text = f'''Hello ,{user_name}, this bot will translate all the words that will 
be sent to it from Cyrillic to Latin, based on the translation 
rules established by the Ministry of Foreign Affairs of Russia'''
    logging.info(f'{user_name=}{user_id=} sent message:{message.text}')
    await message.reply(text)

@dp.message_handler()
async def translit_income(message: types.Message):
    user_name = message.from_user.username
    user_id = message.from_user.id
    text = message.text
    for key in SLOVAR:
        text = text.replace(key, SLOVAR[key])
        result = text
    logging.info(f'{user_name=}, {user_id=} sent message: {text=} bot_return: {result=}')
    await bot.send_message(user_id, result)

if __name__ == '__main__':
    executor.start_polling(dp)

