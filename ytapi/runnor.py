from pathlib import Path

import yaml
from pyyoutube import Client


class Runnor:
    API_KEY = "xyz"  # replace this with your api key.
    default_channel_id = 'UCr3iIpV6Rl3nG0FXCfGXgxQ'  # jakobs kanal

    def __init__(self, secrets_file=None):
        super().__init__()
        if secrets_file is None:
            secrets_file = '/opt/projects/jesper/jesper_project/secrets/secrets.yaml'
        self.secrets = yaml.safe_load(Path(secrets_file).read_text())
        self.API_KEY = self.secrets['youtube']['api_key']
        object
    # channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw" # default google developers channel


class PublicRunnor(Runnor):
    def __init__(self):
        super().__init__()
        print('PublicRunnor')
        self.cli = Client(api_key=self.API_KEY)

    def get_response_dict(self, channel_id=None, parts=None):
        if channel_id is None:
            channel_id = self.default_channel_id
        if parts is None:
            parts = ['id', 'snippet', 'statistics']
        response_dict = self.cli.channels.list(
            channel_id=channel_id, parts=parts, return_json=True
        )
        return response_dict

    def get_response_item0_dict(self, channel_id=None, parts=None):
        response_dict = self.get_response_dict(channel_id=channel_id, parts=parts)
        item0_dict = response_dict["items"][0]
        return item0_dict

    def show_brief_channel_info(self, channel_id=None):
        # # parts = ['snippet']
        # response_dict = self.get_response_dict(channel_id=channel_id)
        # # response_yaml_str = yaml.dump(response_dict, default_flow_style=False)
        # # print(f'\nChannel info \n{response_yaml_str}')
        # # print('----------------------')
        #
        # item0_dict = response_dict["items"][0]
        # # print(f"Channel info: {item0_dict}")
        #
        # # item0_yaml_str = yaml.dump(item0_dict, default_flow_style=False)
        # # print(f'\nChannel info \n{item0_yaml_str}')
        # # print('----------------------')

        item0_dict = self.get_response_item0_dict()
        snippet_dict = item0_dict['snippet']
        props = 'title customUrl publishedAt'.split()
        brief_dict = {prop: snippet_dict[prop] for prop in props}
        brief_yaml_str = yaml.dump(brief_dict, default_flow_style=False)
        print(f'\nBrief channel info:\n{brief_yaml_str}')
        print('----------------------')

    def show_default_channel_info(self, channel_id=None):
        if channel_id is None:
            channel_id = self.default_channel_id

        response_dict = self.cli.channels.list(
            channel_id=channel_id, parts=["id", "snippet", "statistics"], return_json=True
        )
        item0_dict = response_dict["items"][0]
        print(f"Channel info: {item0_dict}")

        item0_yaml_str = yaml.dump(item0_dict, default_flow_style=False)
        print(f'\nChannel info \n{item0_yaml_str}')


class OAuthRunnor(Runnor):
    def __init__(self):
        super().__init__()
        print('OAuthRunnor')

    def upload(self):
        print('upload')


'''
"""
    This example demonstrates how to upload a video.
"""

import pyyoutube.models as mds
from pyyoutube import Client
from pyyoutube.media import Media

# Access token with scope:
# https://www.googleapis.com/auth/youtube.upload
# https://www.googleapis.com/auth/youtube
# https://www.googleapis.com/auth/youtube.force-ssl
ACCESS_TOKEN = "xxx"


def upload_video():
    cli = Client(access_token=ACCESS_TOKEN)

    body = mds.Video(
        snippet=mds.VideoSnippet(title="video title", description="video description")
    )

    media = Media(filename="target_video.mp4")

    upload = cli.videos.insert(
        body=body, media=media, parts=["snippet"], notify_subscribers=True
    )

    response = None
    while response is None:
        print(f"Uploading video...")
        status, response = upload.next_chunk()
        if status is not None:
            print(f"Uploading video progress: {status.progress()}...")

    # Use video class to representing the video resource.
    video = mds.Video.from_dict(response)
    print(f"Video id {video.id} was successfully uploaded.")


if __name__ == "__main__":
    upload_video()

'''


class XyzOAuthRunnor(Runnor):
    # CLIENT_ID = "xxx"  # Your app id
    # CLIENT_SECRET = "xxx"  # Your app secret
    CLIENT_SECRET_PATH = '/opt/projects/jesper/jesper_project/secrets/client_secret.json'  # or your path/to/client_secret_web.json

    SCOPE = [
        "https://www.googleapis.com/auth/youtube",
        "https://www.googleapis.com/auth/youtube.force-ssl",
        "https://www.googleapis.com/auth/userinfo.profile",
    ]

    def __init__(self):
        super().__init__()
        print('OAuthRunnor')
        # self.CLIENT_ID = self.secrets['youtube']['client_id']
        # self.CLIENT_SECRET = self.secrets['youtube']['client_secret']

    def do_authorize(self):
        print('do_authorize')
        # cli = Client(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET)
        cli = Client(client_secret_path=self.CLIENT_SECRET_PATH)
        # response_uri = 'https://mediahead.dk/'
        # authorize_url, state = cli.get_authorize_url(scope=self.SCOPE, redirect_uri=response_uri)
        authorize_url, state = cli.get_authorize_url(scope=self.SCOPE)
        print(f"Click url to do authorize: {authorize_url}")
        # input("trut!")

        response_uri = input("Input youtube redirect uri:\n")
        # response_uri = 'https://localhost/'

        token = cli.generate_access_token(authorization_response=response_uri, scope=self.SCOPE)
        print(f"Your token: {token}")

        # get data
        resp = cli.channels.list(mine=True)
        print(f"Your channel id: {resp.items[0].id}")


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


# region fluff
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
