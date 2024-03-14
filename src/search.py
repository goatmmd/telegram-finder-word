import sys

from telethon.sync import TelegramClient


class SearchWordTelegram:
    def __init__(self, user_api_id, user_api_hash, chat, word):
        self.__api_id = user_api_id
        self.__api_hash = user_api_hash
        self._chat = chat
        self._word = word
        self.client = self.initialize_client()
        self.client.start()

    @property
    def get_word(self):
        return self._word.encode('utf-8')

    @property
    def get_chat(self):
        return self._chat

    def initialize_client(self):
        if sys.platform == 'linux':
            return TelegramClient(f'sessions/{self.__api_id}.session', self.__api_id, self.__api_hash)
        return TelegramClient(f'sessions\{self.__api_id}.session', self.__api_id, self.__api_hash)

    def resolver_chat(self):
        for item in self.client.iter_dialogs():
            if item.name == self._chat:
                return item

    def _find_word(self):
        list_chats = list()

        for message in self.client.iter_messages(self.get_chat, search=self.get_word):
            text = message.text.strip('\n')
            date = message.date.strftime('%Y-%B-%d\t%H:%M:%S')
            list_chats.append(
                {'text': text, 'date': date}
            )

        return list_chats

    def search(self):
        if not self.get_chat.startswith('https://'):
            self._chat = self.resolver_chat()
            return self._find_word()

        return self._find_word()
