"""Script to parse images from telegram channels"""
import uuid

from telethon import TelegramClient, events, sync
from telethon.tl.types import MessageMediaPhoto, PeerChannel

from default_config import config

IMG_DIR = "images/"


def parse_images():
    client = TelegramClient("session_name", config["API_ID"], config["API_HASH"])
    client.start()

    channel = client.get_entity("rand2ch")  # mudak, Lepragram, yaplakal

    c = client.get_entity(PeerChannel(channel.id))

    for message in client.iter_messages(c):
        file_name = IMG_DIR + str(uuid.uuid1())
        # let's get only images
        if type(message.media) == MessageMediaPhoto:
            print(message.download_media(file_name))


if __name__ == "__main__":
    parse_images()
