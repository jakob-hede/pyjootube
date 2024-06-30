import os
from pathlib import Path

import yaml
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRETS_FILE = "/opt/projects/jesper/jesper_project/secrets/ori.client_secret.json"
SCOPES = [
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/userinfo.profile",
]


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server()
    print(credentials)

    props = 'token refresh_token token_uri client_id client_secret scopes'.split()
    data = {prop: getattr(credentials, prop) for prop in props}
    # for prop in props:
    #     print(f'{prop}: "{data[prop]}"')
    yaml_dict = {'google': data}
    yaml_txt = yaml.dump(yaml_dict, default_flow_style=False)
    print()
    print(yaml_txt)
    yaml_txt = get_quoted_yaml(yaml_dict)
    print()
    print(yaml_txt)
    print()
    return build('youtube', 'v3', credentials=credentials)


def get_quoted_yaml(_data):
    import yaml
    from yaml.representer import SafeRepresenter

    class QuotedStrDumper(yaml.SafeDumper):
        pass

    class QuotedString(str):
        pass

    def quoted_str_presenter(dumper, data_):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data_, style='"')

    def dict_representer(dumper, data_):
        new_data = {}
        for k, v in data_.items():
            if isinstance(v, str):
                new_data[k] = QuotedString(v)
            elif isinstance(v, list):
                new_data[k] = [QuotedString(i) if isinstance(i, str) else i for i in v]
            else:
                new_data[k] = v
        return dumper.represent_dict(new_data.items())

    QuotedStrDumper.add_representer(QuotedString, quoted_str_presenter)
    QuotedStrDumper.add_representer(dict, dict_representer)
    yaml_txt = yaml.dump(_data, default_flow_style=False, Dumper=QuotedStrDumper)
    return yaml_txt


def main():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    # print()
    # print(service)


def test_main():
    secrets_file = '/opt/projects/jesper/jesper_project/secrets/secrets.yaml'
    in_yaml_txt = Path(secrets_file).read_text()
    yaml_data = yaml.safe_load(in_yaml_txt)
    print(yaml_data)
    # print(in_yaml_txt)
    out_yaml_txt = get_quoted_yaml(yaml_data)
    print(out_yaml_txt)
    yaml_data = yaml.safe_load(out_yaml_txt)
    out_yaml_txt = get_quoted_yaml(yaml_data)
    print(out_yaml_txt)


if __name__ == '__main__':
    main()
    # test_main()
