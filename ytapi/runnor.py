from pathlib import Path

import yaml


class Runnor:
    API_KEY = "xyz"  # replace this with your api key.
    default_channel_id = 'UCr3iIpV6Rl3nG0FXCfGXgxQ'  # jakobs kanal
    # channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw" # default google developers channel

    def __init__(self, secrets_file=None):
        super().__init__()
        if secrets_file is None:
            secrets_file = '/opt/projects/jesper/jesper_project/secrets/secrets.yaml'
        self.secrets = yaml.safe_load(Path(secrets_file).read_text())
        self.API_KEY = self.secrets['youtube']['api_key']
        object


# region fluff
# class XyzOAuthRunnor(Runnor):
#     # CLIENT_ID = "xxx"  # Your app id
#     # CLIENT_SECRET = "xxx"  # Your app secret
#     CLIENT_SECRET_PATH = '/opt/projects/jesper/jesper_project/secrets/client_secret.json'  # or your path/to/client_secret_web.json
#
#     SCOPE = [
#         "https://www.googleapis.com/auth/youtube",
#         "https://www.googleapis.com/auth/youtube.force-ssl",
#         "https://www.googleapis.com/auth/userinfo.profile",
#     ]
#
#     def __init__(self):
#         super().__init__()
#         print('OAuthRunnor')
#         # self.CLIENT_ID = self.secrets['youtube']['client_id']
#         # self.CLIENT_SECRET = self.secrets['youtube']['client_secret']
#
#     def do_authorize(self):
#         print('do_authorize')
#         # cli = Client(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET)
#         cli = Client(client_secret_path=self.CLIENT_SECRET_PATH)
#         # response_uri = 'https://mediahead.dk/'
#         # authorize_url, state = cli.get_authorize_url(scope=self.SCOPE, redirect_uri=response_uri)
#         authorize_url, state = cli.get_authorize_url(scope=self.SCOPE)
#         print(f"Click url to do authorize: {authorize_url}")
#         # input("trut!")
#
#         response_uri = input("Input youtube redirect uri:\n")
#         # response_uri = 'https://localhost/'
#
#         token = cli.generate_access_token(authorization_response=response_uri, scope=self.SCOPE)
#         print(f"Your token: {token}")
#
#         # get data
#         resp = cli.channels.list(mine=True)
#         print(f"Your channel id: {resp.items[0].id}")


#         # or if you want to use a web type client_secret.json
#         # cli = Client(client_secret_path=CLIENT_SECRET_PATH)
#
#         authorize_url, state = cli.get_authorize_url(scope=self.SCOPE)
#         print(f"Click url to do authorize: {authorize_url}")
#
#         response_uri = input("Input youtube redirect uri:\n")
#
#         token = cli.generate_access_token(authorization_response=response_uri, scope=self.SCOPE)
#         print(f"Your token: {token}")
#
#         # get data
#         resp = cli.channels.list(mine=True)
#         print(f"Your channel id: {resp.items[0].id}

"""
    This example demonstrates how to retrieve information for a channel.
"""

# from pyjootube.pyyoutube import Client


# def get_channel_info():
#     cli = Client(api_key=API_KEY)
#
#     # channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw" # default google developers channel
#     channel_id = 'UCr3iIpV6Rl3nG0FXCfGXgxQ'  # jakobs kanal
#
#     response_dict = cli.channels.list(
#         channel_id=channel_id, parts=["id", "snippet", "statistics"], return_json=True
#     )
#     item0_dict = response_dict["items"][0]
#     print(f"Channel info: {item0_dict}")
#
#     item0_yaml_str = yaml.dump(item0_dict, default_flow_style=False)
#     print()
#     print(f'Channel info \n{item0_yaml_str}')
#
# # if __name__ == "__main__":
# #     get_channel_info()

# endregion fluff
