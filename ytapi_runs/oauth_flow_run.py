from ytapi.runnor import  OAuthRunnor


def main():
    runnor = OAuthRunnor()
    # runnor.show_default_channel_info()
    runnor.show_brief_channel_info()


if __name__ == "__main__":
    main()

# """
#     This example demonstrates how to retrieve information for a channel.
# """
# import yaml
#
# # from pyjootube.pyyoutube import Client
#
# from pyyoutube import Client
#
# API_KEY = "AIzaSyBbEoFYabI_59-Wrtyt98F6fG05HNX3XeQ"  # replace this with your api key.
#
#
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
