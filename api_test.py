import pytest

from app import app

def test_api_posts():
    response = app.test_client().get('/api/posts/')
    # проверка на list
    assert type(response.json) == list, 'полученные данные не являются list'

    # проверка на вхождение ключей в каждом посте, который получили из response = app.test_client().get('/api/posts/')
    keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    for post in response.json:
        for key in keys:
            assert key in post, f'ключ "{key}" не найден'


def test_api_post_1():
    response = app.test_client().get('/api/posts/1')
    # проверка на dict
    assert type(response.json) == dict

    # проверка на ключи
    keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
    for i in keys:
        assert i in response.json.keys(), f'ключ "{i}"  не найден'
