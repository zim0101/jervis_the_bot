import requests
from settings import GITHUB_ACCESS_TOKEN


headers = {
    'Authorization': GITHUB_ACCESS_TOKEN
}


def authenticate():

    with requests.Session() as s:
        s.headers.update(headers)
        resp = s.get('https://api.github.com')
        print(resp.content.decode())


def get_repo_list():
    with requests.Session() as s:
        resp = s.post('https://api.github.com/zim0101/repos', data={
            "name": "test_repo_using_api"
        })
        print(resp.content.decode())


if __name__ == '__main__':
    authenticate()
    get_repo_list()
