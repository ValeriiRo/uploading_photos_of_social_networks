import requests
import os
import json
import time
from tqdm import tqdm

def information_file():
    if os.path.exists('information_file'):
        pass
    else:
        os.mkdir('information_file')
    file_path = os.path.join(os.getcwd(), "information_file", "information_file.json")
    new_file = open(file_path, "w", encoding="UTF-8")
    new_file.write

def Saving_information_file(type_file, like):
    with open("information_file/information_file.json", 'a') as write_file:
        data = [{
                    "file_name": like + ".jpg",
                     "size": type_file
                     }]
        json.dump(data, write_file)

def YaUpLoader(list_photo):
    API_BASE_URL = 'https://cloud-api.yandex.net/'
    token = input('Введите токен Яндекс.Диска: ')
    name_list = []
    for photo in tqdm(list_photo):
        like = str(photo['likes']['count'])
        if like in name_list:
            like += '_'
            like += str(photo['date'])
        name_list.append(like)
        up_photo = photo['sizes']
        max_height = 0
        max_width = 0
        for max_sizes in up_photo:
            if max_height < max_sizes['height'] and max_width < max_sizes['width']:
                max_height = max_sizes['height']
                max_width = max_sizes['width']
                max_sizes_photo = max_sizes['url']
                type_file = max_sizes['type']
        Saving_information_file(type_file, like)
        headers = {
            'authorization': f'OAuth {token}',
            "href": "string",
            "method": "string",
            "templated": 'true',
             }
        params = {'path': 'photos_social_networks/' + like,
                  "url": max_sizes_photo
                  }
        path = {'path': 'photos_social_networks'}
        requests.put(API_BASE_URL + 'v1/disk/resources', headers=headers, params=path)
        requests.post(API_BASE_URL + 'v1/disk/resources/upload', params=params, headers=headers)
        time.sleep(1)

def uploading_a_photo(id_user):
    params = {
        'user_id': id_user,
        'access_token': '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008',
        'album_id': 'profile',
        'extended': 1,
        'count': count,
        'photo_sizes': 1,
        'no_service_albums': 0,
        'need_hidden': 0,
        'skip_hidden': 0,
        'v': 5.131
    }
    request_photo = requests.get(url + 'photos.get', params=params)
    list_photo = request_photo.json()['response']['items']
    YaUpLoader(list_photo)

information_file()
url = 'https://api.vk.com/method/'
id_user = input('Введите id профеля: ')
count = input('Введите количество фотографий для загрузки: ')
uploading_a_photo(id_user)