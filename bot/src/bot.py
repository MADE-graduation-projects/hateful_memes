import telebot
from PIL import Image

from default_config import config
from utils import Db_connection

images = None
img_id = None


def get_next_image(bot, message, images, user_id):
    img = images.pop()
    img_id, img_uri = img[0], img[1]
    img_path = "imgs/bot_images/" + img_uri
    bot.send_chat_action(message.from_user.id, "upload_photo")
    bot.send_photo(message.from_user.id, Image.open(img_path))
    return img_id


def get_user_id(message):
    return message.from_user.id


def add_user(chat_id):
    conn.execute(
        f"INSERT INTO images.users (chat_id) VALUES ({chat_id}) ON CONFLICT (chat_id) DO NOTHING")
    conn.commit()


def get_unique_images_from_db(user_id):
    return conn.fetchall(
        f"select * from images.images i where not exists (select 1 from images.user_interactions ui where ui.image_id = i.id and ui.user_id = {user_id}) order by random()"
    )


def get_reaction(img_id, user_id, react):
    conn.execute(
        f"insert into images.user_interactions (image_id, user_id, react) values ({img_id}, {user_id}, {react})"
    )
    conn.commit()


if __name__ == "__main__":
    bot = telebot.TeleBot(config["BOT_TOKEN"])
    conn = Db_connection()

    @bot.message_handler(commands=["start"])
    def handle_start(message):
        chat_id = get_user_id(message)
        add_user(chat_id)  # add used to database if not existed

        global images
        images = get_unique_images_from_db(chat_id)

        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("/go", "/help", "/stop")
        user_markup.row("не токсик", "не мем", "уже было", "пропустить")
        user_markup.row("насилие", "ксенофобия", "алко-нарко", "мизогиния")
        user_markup.row("суицид", "порно", "токсик текст", "токсик (иное)")
        bot.send_message(
            message.from_user.id,
            """Привет, го размечать смешные картинки!
Наша цель собрать датасет мемов на <b>русском языке</b>.
Если увидишь что-то по-английски (или на другом языке) пожалуйста нажимай <b><i>не мем</i></b>.
Если на картинке только текст и нет изображения пожалуйста нажимай <b><i>не мем</i></b>.
Суть разметки заключается в определении токсичный мем или нет.
Токсичным мы называем контент, который:
<i>
(a) содержит угрозы, призывы к насилию
(б) содержит порнографические и эротические изображения и тексты, сцены сексуального характера
(в) содержит сцены жестокого обращения с животными
(г) содержит описание средств и способов суицида, любое подстрекательство к его совершению
(д) способствует разжиганию расовой ненависти или вражды
(е) способствует разжиганию религиозной ненависти или вражды
(ж) способствует разжиганию этнической ненависти или вражды
(з) способствует разжиганию по признакам отнесения к определенному полу
(и) способствует разжиганию по признакам отнесения к определенной ориентации
(к) способствует разжиганию по иным индивидуальным признакам и особенностям человека (включая вопросы его здоровья)
(л) пропагандирует преступную деятельность или содержит советы, инструкции или руководства по совершению преступных действий
(м) описывает привлекательность употребления наркотических веществ
(н) может вызвать чувства неприятия или отвращения
</i>
Если ты что-то забыл, просто нажми /help и я продублирую это сообщение""",
            parse_mode="html",
            reply_markup=user_markup,
        )

    @bot.message_handler(commands=["help"])
    def handle_stop(message):
        bot.send_message(
            message.from_user.id,
            """Наша цель собрать датасет мемов на <b>русском языке</b>.
Если увидишь что-то по-английски (или на другом языке) пожалуйста нажимай <b><i>не мем</i></b>.
Если на картинке только текст и нет изображения пожалуйста нажимай <b><i>не мем</i></b>.
Суть разметки заключается в определении токсичный мем или нет.
Токсичным мы называем контент, который:
<i>
(a) содержит угрозы, призывы к насилию
(б) содержит порнографические и эротические изображения и тексты, сцены сексуального характера
(в) содержит сцены жестокого обращения с животными
(г) содержит описание средств и способов суицида, любое подстрекательство к его совершению
(д) способствует разжиганию расовой ненависти или вражды
(е) способствует разжиганию религиозной ненависти или вражды
(ж) способствует разжиганию этнической ненависти или вражды
(з) способствует разжиганию по признакам отнесения к определенному полу
(и) способствует разжиганию по признакам отнесения к определенной ориентации
(к) способствует разжиганию по иным индивидуальным признакам и особенностям человека (включая вопросы его здоровья)
(л) пропагандирует преступную деятельность или содержит советы, инструкции или руководства по совершению преступных действий
(м) описывает привлекательность употребления наркотических веществ
(н) может вызвать чувства неприятия или отвращения
</i>""",
            parse_mode="html",
        )

    @bot.message_handler(commands=["stop"])
    def handle_stop(message):
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(
            message.from_user.id,
            "Пока... возвращайся, тут ещё куча картинок для разметки. Если передумаешь, просто напиши /start",
            reply_markup=hide_markup,
        )

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        global img_id

        user_id = get_user_id(message)

        if message.text == "/go":
            bot.send_message(message.from_user.id, "погнали!")

        if message.text == "не мем":
            react = 3
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id, "понял, это не мем(")

        if message.text == "уже было":
            react = 2
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id, "понял, такое уже было(")

        if message.text == "токсик (иное)":
            react = 1
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id, "понял, это токсичный мем(")

        if message.text == "не токсик":
            react = 0
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id, "понял, это хорошие мем)")

        if message.text == "насилие":
            react = 4
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id,
                             "понял, тут какая-то жесть()")

        if message.text == "ксенофобия":
            react = 5
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id,
                             "понял, тут разжигают ненависть(")

        if message.text == "алко-нарко":
            react = 6
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id,
                             "понял, тут какие-то вещества(")

        if message.text == "мизогиния":
            react = 7
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id,
                             "понял, тут женоненавистничество(")

        if message.text == "суицид":
            react = 8
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id,
                             "понял, тут толкают к суициду(")

        if message.text == "порно":
            react = 9
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id,
                             "понял, тут эротика или порно)")

        if message.text == "токсик текстк":
            react = 10
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id,
                             "понял, картинка норм, а текст токсичный(")

        img_id = get_next_image(bot, message, images, user_id)

    bot.infinity_polling()
