from ytapi.runnor import  OAuthRunnor


def main():
    runnor = OAuthRunnor()
    # runnor.show_default_channel_info()
    runnor.upload()


if __name__ == "__main__":
    main()
