import requests

heroes_list = ['Hulk', 'Captain America', 'Thanos']
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
resp = requests.get(url)
heroes = resp.json()
heroes_dict = []

for hero in heroes_list:
    for power_stats in heroes:
        if hero in power_stats['name']:
            heroes_dict.append({'name': power_stats['name'],
                                'intelligence': power_stats['powerstats']['intelligence']})
    most_intelligence = 0
    name = ''
    for intelligence_hero in heroes_dict:
        if most_intelligence < int(intelligence_hero['intelligence']):
            most_intelligence = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']


class YaUploader:
    def __init__(self, token):
        self.token = token
    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, disk_file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self.get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')



if __name__ == '__main__':
    print('### Task 1 ###')
    print(f'Самый умный герой - {name}, интеллект: {most_intelligence}')

    # Не понял как найти только 'hulk'
    for name in heroes_dict:
        print(name)

    print('### Task 2 ###')
    path_to_file = ''
    token = ''
    ya = YaUploader(token)
    result = ya.upload(path_to_file, path_to_file)



