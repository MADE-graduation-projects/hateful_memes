import telebot
from PIL import Image

from default_config import config
from utils import Db_connection

images = None
img_id = None


def get_next_image(bot, message, images, user_id):
    img = images.pop()
    img_id, img_uri = img[0], img[1]
    bot.send_chat_action(message.from_user.id, "upload_photo")
    bot.send_photo(message.from_user.id, Image.open(img_uri))
    return img_id


def get_user_id(message):
    return message.from_user.id


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
        user_id = get_user_id(message)
        global images
        images = get_unique_images_from_db(user_id)

        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("/go", "/stop")
        user_markup.row("не мем", "уже было")
        user_markup.row("токсик", "не токсик")
        bot.send_message(
            message.from_user.id,
            """Привет, го размечать смешные картинки!
Наша цель собрать датасет мемов на <b>русском языке</b>.
Если увидишь что-то по-английски (или на другом языке) пожалуйста нажимай <b><i>не мем</i></b>
Если на картинке только текст и нет изображения пожалуйста нажимай <b><i>не мем</i></b>""",
            parse_mode="html",
            reply_markup=user_markup,
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

        if message.text == "токсик":
            react = 1
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id, "понял, это токсичный мем(")

        if message.text == "не токсик":
            react = 0
            get_reaction(img_id, user_id, react)
            bot.send_message(message.from_user.id, "понял, это хорошие мем)")

        img_id = get_next_image(bot, message, images, user_id)

    bot.infinity_polling()
