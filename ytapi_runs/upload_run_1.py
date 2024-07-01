from ytapi.oauth_runnor import OAuthRunnor


def main():
    runnor = OAuthRunnor()
    # runnor.show_default_channel_info()
    # runnor.upload_ytdl('beating')
    runnor.delete_ytdl('beating')


if __name__ == "__main__":
    main()
