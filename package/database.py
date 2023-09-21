import os
import re
import sqlite3

from package import CHATS_PATH, config

thisFile = os.path.realpath(__file__)
wd = os.path.dirname(thisFile)


class Database:
    def __init__(self, filePath=""):
        def regexp(expr, item):
            reg = re.compile(expr, flags=re.IGNORECASE)
            return reg.search(item) is not None
        defaultFilePath = config.chatGPTApiLastChatDatabase if config.chatGPTApiLastChatDatabase and os.path.isfile(
            config.chatGPTApiLastChatDatabase) else os.path.join(CHATS_PATH, "default.chat")
        self.filePath = filePath or defaultFilePath
        self.connection = sqlite3.connect(self.filePath)
        self.connection.create_function("REGEXP", 2, regexp)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS data (id TEXT PRIMARY KEY, title TEXT, content TEXT)')
        self.connection.commit()

    def insert(self, id, title, content):
        self.cursor.execute('SELECT * FROM data WHERE id = ?', (id,))
        existing_data = self.cursor.fetchone()
        if existing_data:
            if existing_data[1] == title and existing_data[2] == content:
                return
            else:
                self.cursor.execute(
                    'UPDATE data SET title = ?, content = ? WHERE id = ?', (title, content, id))
                self.connection.commit()
        else:
            self.cursor.execute(
                'INSERT INTO data (id, title, content) VALUES (?, ?, ?)', (id, title, content))
            self.connection.commit()

    def search(self, title, content):
        if config.regexpSearchEnabled:
            # with regular expression
            self.cursor.execute(
                'SELECT * FROM data WHERE title REGEXP ? AND content REGEXP ?', (title, content))
        else:
            # without regular expression
            self.cursor.execute('SELECT * FROM data WHERE title LIKE ? AND content LIKE ?',
                                ('%{}%'.format(title), '%{}%'.format(content)))
        return self.cursor.fetchall()

    def delete(self, id):
        self.cursor.execute('DELETE FROM data WHERE id = ?', (id,))
        self.connection.commit()

    def clear(self):
        self.cursor.execute('DELETE FROM data')
        self.connection.commit()
