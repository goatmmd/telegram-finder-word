# -------------- local module ----------
from config_handler import load_config
from src.account_handler import Account
from src.search import SearchWordTelegram
from src.tk_handler import get_word_input, get_links_input
from src.file_writer import DocxWriter
# --------------------------------------


if __name__ == "__main__":
    print('Start...!')
    app_config = load_config()
    account = Account(api_id=app_config['ApiId'], api_hash=app_config['ApiHash'])
    chat = get_links_input()
    word = get_word_input()
    # --------------------------------------------------------------

    # ---------------------------------------------------------------

    instance_finder = SearchWordTelegram(account.api_id, account.api_hash, chat, word)
    print(f'Searching {word} from {chat}')
    raw_data = instance_finder.search()

    writer = DocxWriter(raw_data, chat, word)
    writer.write_to_file()
    print('Finished')
