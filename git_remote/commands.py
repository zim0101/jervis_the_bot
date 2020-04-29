import requests


headers = {
    'Authorization': 'token <personal access token>'
}


def create_repo():
    with requests.Session() as s:
        s.headers.update(headers)
        resp = s.post('https://api.github.com/user/repos', json={
            "name": "test_repo_using_api"
        })
        print(resp.content.decode())


if __name__ == '__main__':
    # authenticate()
    create_repo()
