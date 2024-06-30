import yaml
from pyyoutube import Client


class Runnor:
    API_KEY = "AIzaSyBbEoFYabI_59-Wrtyt98F6fG05HNX3XeQ"  # replace this with your api key.
    jakobs_channel_id = 'UCr3iIpV6Rl3nG0FXCfGXgxQ'  # jakobs kanal

    def __init__(self):
        super().__init__()
        print('Runnor')
        self.cli = Client(api_key=self.API_KEY)

    def show_brief_channel_info(self, channel_id=None):
        if channel_id is None:
            channel_id = self.jakobs_channel_id
        response_dict = self.cli.channels.list(
            channel_id=channel_id, parts=['snippet'], return_json=True
        )
        # response_yaml_str = yaml.dump(response_dict, default_flow_style=False)
        # print(f'\nChannel info \n{response_yaml_str}')
        # print('----------------------')

        item0_dict = response_dict["items"][0]
        # print(f"Channel info: {item0_dict}")

        # item0_yaml_str = yaml.dump(item0_dict, default_flow_style=False)
        # print(f'\nChannel info \n{item0_yaml_str}')
        # print('----------------------')

        snippet_dict = item0_dict['snippet']
        props = 'title customUrl publishedAt'.split()
        brief_dict = {prop: snippet_dict[prop] for prop in props}
        brief_yaml_str = yaml.dump(brief_dict, default_flow_style=False)
        print(f'\nBrief channel info:\n{brief_yaml_str}')
        print('----------------------')

    def show_default_channel_info(self, channel_id=None):
        if channel_id is None:
            channel_id = self.jakobs_channel_id
        # channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw" # default google developers channel
        # channel_id = 'UCr3iIpV6Rl3nG0FXCfGXgxQ'  # jakobs kanal

        response_dict = self.cli.channels.list(
            channel_id=channel_id, parts=["id", "snippet", "statistics"], return_json=True
        )
        item0_dict = response_dict["items"][0]
        print(f"Channel info: {item0_dict}")

        item0_yaml_str = yaml.dump(item0_dict, default_flow_style=False)
        print(f'\nChannel info \n{item0_yaml_str}')


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
