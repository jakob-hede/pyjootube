import yaml

from pyyoutube import Client
from ytapi.runnor import Runnor


class ApikeyRunnor(Runnor):
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
