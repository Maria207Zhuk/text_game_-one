from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters

# Production token
BOT_TOKEN_PROD = '5450702903:AAHnRqIvqAJTNNmBt4Cqdedi-VSRcuNpfLI'
updater = Updater(BOT_TOKEN_PROD, use_context=True)

steat = 1

food = 0
ak_47 = 0
posion = 0
 
def start_handler(update: Update, context: CallbackContext): 
    global steat
    if steat == 1:
        context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Привіт, {update.effective_chat.first_name}, ми раді вас зустріти тут! Ви потрапили у світ, де потрібно вижити за буть-яких умов, використовуючи усі можливі варіанти які існують у цій грі.  !")   
        context.bot.send_message(chat_id=update.effective_chat.id,  text="В тебе запаси їжі,  автомат АК-47, не смертельна отрута, зілля доброти.")   
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Ти ідеш в магазин, щоб купити їжу, але по дорозі ти зустрів чоловіка, який вбиває поглядом. ")
        button = [[KeyboardButton("оборонятись")],[KeyboardButton("здатись")],[KeyboardButton("застосувати автомат і більше ніяких перешкоджень")]]
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Твій вибір, 1 – оборонятись, 2 – здатись, 3 – застосувати автомат і більше ніяких перешкоджень.",
        reply_markup = ReplyKeyboardMarkup(button)) 
        steat += 1

def message_handler(update: Update, context: CallbackContext): 
    global steat
    message = update.message.text
    if steat == 2:
        if message == 'оборонятись':
            context.bot.send_message(update.effective_chat.id, text="Перемога! Ви сильна людина, яка завжди може себе захистити.")
        elif message == "здатись":
            context.bot.send_message(update.effective_chat.id, text="Ви програли! Ви слабка людина.")
        elif message == "застосувати автомат і більше ніяких перешкоджень":
            context.bot.send_message(update.effective_chat.id, text="Перемога! Ви жорстока людина, яка не пропаде у світі.")
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Ти захворів, тому ти нарвав лікувальні трави, щоб зробити мазь, але коли ти їх збирав, до тебе підкрався птах та вирвав з твоїх рук усе лікувальне гілля та трави.")   
        button = [[KeyboardButton("змиритись, та назбирати трави знову")],[KeyboardButton("застосувати автомат")],[KeyboardButton("заманити їжею")]]
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Твій вибір: 1 – змиритись, та назбирати трави знову, 2 – застосувати автомат, 3- заманити їжею.",
        reply_markup = ReplyKeyboardMarkup(button))
        steat += 1
    elif steat == 3:
        if message == 'змиритись, та назбирати трави знову':
            context.bot.send_message(update.effective_chat.id, text="Перемога ваша! Ви могли вернути свої трави, але через свою невпененність, робите все заново.")
        elif message == "застосувати автомат":
            context.bot.send_message(update.effective_chat.id, text="Перемога ваша! Ви жорстока людина, яка добивається свого.")
        elif message == "заманити їжею":
            context.bot.send_message(update.effective_chat.id, text="Перемога ваша! Ви хитра людина, яка завжди перемагає.")
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Ти їхав на роботу, але по дорозі у тебе скінчилось паливо, до наступної заправки 50 км.")   
        button = [[KeyboardButton("ти маєш запаси їжі, можеш почекати, коли по тебе приїдуть")],[KeyboardButton("ти можеш відібрати машину у людей, та злити паливо")],[KeyboardButton("ти можеш отруїти людей, та злити паливо")],[KeyboardButton("ти можеш дати людям зілля доброти, та вони тобі допоможуть")]]
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Твій вибір, 1 -  ти маєш запаси їжі, можеш почекати, коли по тебе приїдуть,  2 – ти можеш відібрати машину у людей, та злити паливо, 3 – ти можеш отруїти людей, та злити паливо, 4 – ти можеш дати людям зілля доброти, та вони тобі допоможуть.",
        reply_markup = ReplyKeyboardMarkup(button))
        steat += 1
    elif steat == 4:
        if message == 'ти маєш запаси їжі, можеш почекати, коли по тебе приїдуть':
            context.bot.send_message(update.effective_chat.id, text="Ти програв! Ти легковажна людина, яка надіється на чужу допомогу.")
        elif message == "ти можеш відібрати машину у людей та злити паливо":
            context.bot.send_message(update.effective_chat.id, text="Ти програв! Ти шукаєш у всьому вигоду і готовий піти на все, пожертвуючи чужим життям.")
        elif message == "ти можеш отруїти людей та злити паливо":
            context.bot.send_message(update.effective_chat.id, text="Ти програв! Твоя користь важливіша за життя людей.")
        elif message == "ти можеш дати людям зілля доброти, та вони тобі допоможуть":
            context.bot.send_message(update.effective_chat.id, text="Перемога! Ти хитра людина, яка може знайти підхід.")
        context.bot.send_message(update.effective_chat.id, text="вітаю! Ви пройшли гру")
        steat = 1
    


start_command_handler = CommandHandler("start", start_handler) 
updater.dispatcher.add_handler(start_command_handler) 

text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler) 
updater.dispatcher.add_handler(text_handler) 
 
# Start bot 
updater.start_polling()