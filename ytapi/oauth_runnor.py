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
        # self.cli = Client(access_token=self.ACCESS_TOKEN)
        self.ytdl: Ytdl | None = None
        self.video_file: Path | None = None
        self.title: str | None = None
        self.description: str | None = None
        self.upload_id: str | None = None

    @property
    def cli(self):
        cli = Client(access_token=self.ACCESS_TOKEN)
        return cli

    def upload_ytdl(self, ytdl_name):
        print(f'upload_ytdl "{ytdl_name}"')
        self.init_ytdl(ytdl_name)
        self.upload_video(self.video_file, title=self.title, description=self.description)

    def delete_ytdl(self, ytdl_name):
        self.init_ytdl(ytdl_name)
        # How to delete a video?
        self.delete_video(self.upload_id)

    def init_ytdl(self, ytdl_name):
        self.ytdl = Ytdl.post_factory(ytdl_name)
        # ytdl.print_analysis()
        # # analysis = ytdl.analysis()
        # # # print(f'analysis: {analysis}')
        # # for line in analysis:
        # #     print(f'- {line}')
        # # print()
        self.video_file = self.ytdl.get_video_file()
        # print(f'video_file: {self.video_file}')
        info_json = self.ytdl.get_fixed_json_info()
        self.title = info_json['title']
        self.description = info_json['description']
        uploaded_json = self.ytdl.get_uploaded_json()
        print(f'uploaded_json: {uploaded_json}')
        if uploaded_json:
            self.upload_id = uploaded_json['id']

    def upload_video(self, file, title='video title', description='video description'):
        if self.upload_id:
            self.delete_video(self.upload_id)

        body = mds.Video(
            snippet=mds.VideoSnippet(title=title, description=description),
            # # status=mds.VideoStatus(privacyStatus="public"),  # Set video as not private
            status=mds.VideoStatus(privacyStatus="public", madeForKids=False)
            # Set video as not private and not for kids
        )

        media = Media(filename=str(file))

        upload = self.cli.videos.insert(
            # body=body, media=media, parts=["snippet"], notify_subscribers=True
            body=body, media=media, parts=["snippet", "status"], notify_subscribers=True
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
        self.ytdl.write_uploaded_json(response)

    def delete_video(self, upload_id):
        pass
        # How to delete a video? Get hints from upload_video

        result = None
        try:
            result = self.cli.videos.delete(video_id=upload_id)
        except Exception as e:
            print(f'Exception: {e}')
            # return
        # result = self.cli.videos.delete(video_id=upload_id)
        self.ytdl.obsolize_uploaded()
        if result:
            print(f'Video with id {upload_id} was successfully deleted.')
        else:
            print(f'Failed to delete video with id {upload_id}.')

        # # response = None
        # # status: MediaUploadProgress
        # # response: dict
        # # while response is None:
        # #     print(f"Deletring video...")
        # #     status, response = actor.
        # #     if status is not None:
        # #         print(f"Uploading video progress: {status.progress()}...")
        # #
        # # print(f'response: {response}')
        # #
        # #
        # # cli.videos.delete(id=upload_id)
        # print(f'Video with id {upload_id} was successfully deleted.')


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
