from pathlib import Path

from pyyoutube import Client
import pyyoutube.models as mds
from pyyoutube.media import Media, MediaUploadProgress

from ytapi.runnor import Runnor
from yt_code.ytdl.ytdl import Ytdl


class OAuthRunnor(Runnor):
    def __init__(self):
        super().__init__()
        print('OAuthRunnor')
        self.ACCESS_TOKEN = self.secrets['google']['token']
        self.ytdl: Ytdl | None = None
        self.video_file: Path | None = None
        self.title: str | None = None
        self.description: str | None = None

    def upload_ytdl(self, ytdl_name):
        print(f'upload_ytdl "{ytdl_name}"')
        self.init_ytdl(ytdl_name)
        self.upload_video(self.video_file, title=self.title, description=self.description)

    def delete_ytdl(self, ytdl_name):
        self.init_ytdl(ytdl_name)
        # How to delete a video?

    def init_ytdl(self, ytdl_name):
        ytdl = Ytdl.post_factory(ytdl_name)
        # ytdl.print_analysis()
        # # analysis = ytdl.analysis()
        # # # print(f'analysis: {analysis}')
        # # for line in analysis:
        # #     print(f'- {line}')
        # # print()
        self.video_file = ytdl.get_video_file()
        # print(f'video_file: {self.video_file}')
        info_json = ytdl.get_fixed_json_info()
        self.title = info_json['title']
        self.description = info_json['description']
        uploaded_json = ytdl.get_uploaded_json()
        print(f'uploaded_json: {uploaded_json}')

    def upload_video(self, file, title='video title', description='video description'):
        cli = Client(access_token=self.ACCESS_TOKEN)

        body = mds.Video(
            snippet=mds.VideoSnippet(title=title, description=description)
        )

        media = Media(filename=str(file))

        upload = cli.videos.insert(
            body=body, media=media, parts=["snippet"], notify_subscribers=True
        )

        response = None
        status: MediaUploadProgress
        response: dict
        while response is None:
            print(f"Uploading video...")
            status, response = upload.next_chunk()
            if status is not None:
                print(f"Uploading video progress: {status.progress()}...")

        print(f'response: {response}')
        # Use video class to representing the video resource.
        video = mds.Video.from_dict(response)
        print(f'Video id {video.id} was successfully uploaded.')


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
