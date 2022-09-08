import psycopg2
import psycopg2.extras

from default_config import config


class Db_connection:
    def __init__(self):
        self.connection = psycopg2.connect(
            password=config["DB_PASS"],
            host=config["DB_HOST"],
            dbname=config["DB_NAME"],
            user=config["DB_USERNAME"],
            port=config["DB_PORT"],
        )
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def execute(self, script):
        return self.cursor.execute(script)

    def fetchall(self, script):
        self.cursor.execute(script)
        return self.cursor.fetchall()

    def fetchone(self, script):
        self.cursor.execute(script)
        res = self.cursor.fetchone()
        if res is None:
            return {}
        else:
            return dict(res)
