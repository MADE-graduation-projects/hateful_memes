import os
import pprint

config = {
    "DB_HOST": os.environ["DB_HOST"],
    "DB_NAME": os.environ["DB_NAME"],
    "DB_USERNAME": os.environ["DB_USERNAME"],
    "DB_PORT": os.environ["DB_PORT"],
    "DB_PASS": os.environ["DB_PASS"],
    "BOT_TOKEN": os.environ["BOT_TOKEN"],
    "API_ID": os.environ["API_ID"],
    "API_HASH": os.environ["API_HASH"],
}

pprint.pprint(config)
