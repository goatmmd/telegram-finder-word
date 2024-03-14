import json


def load_config():
    try:
        with open('configs.json') as f:
            config = json.loads(f.read())['Account']
            if config['ApiId'] == 0 or config['ApiHash'] == '':
                raise Exception("Please fill the api id and api hash in `configs.json` ")
            return config
    except Exception as err:
        raise Exception(f'Error while loading account config... `Call with maintainer`:\n ({err})')
