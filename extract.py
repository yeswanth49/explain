import requests
import base64


def extract(repo_owner,repo_name,file_path):

    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'

    response = requests.get(url)

    if response.status_code ==200:
        file_data = response.json()
        file_content = file_data['content']

        decoded_content = base64.b64decode(file_content).decode('utf-8')
        print(decoded_content)

    else :
        print('request failed')

def main():
    owner = input('owner?')
    name = input('repo name?')
    path = input('path?')
    extract(owner,name,path)


if __name__ == '__main__':
    main()
