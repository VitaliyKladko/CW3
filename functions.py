import json

def open_json(file) -> list:
    """
    Функция производит чтение данных из .json файла, загружает все посты
    :param file: Файл .json, который необходимо прочитать
    :return: данные из файла .json
    """
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)

    return json_data

def get_posts_by_user(posts_data, user_name) -> list:
    """
    Функция отдаст пост, который соответствует определенному пользователю (имени пользователя)
    :param posts_data: Данные о размещенных на сайте постах из data.json
    :param user_name: Параметр, соответствующий идентификатору
    :return: Пост, который соответствует user_name
    """
    output_post = []
    for post in posts_data:
        if user_name == post['poster_name']:
            output_post.append(post)

    return output_post

def get_comments_by_post_id(comment_data: list, post_id: int) -> list:
    """
    Функция возвращает комментарии определенного поста по его ID
    :param comment_data: Список словарей комментариев -> list
    :param post_id: номер поста (его ID) -> int
    :return: Список словарей
    """
    output_comments = []
    for comment in comment_data:
        if post_id == comment['post_id']:
            output_comments.append(comment)

    return output_comments

def search_for_posts(posts_data: list, query: str) -> list:
    """
    Функция возвращает список постов по ключевому слову
    :param posts_data: Данные о размещенных на сайте постах из data.json -> list
    :param query: Слово, по которому происходит поиск -> str
    :return:output_post -> список постов, с которыми есть совпадение
    """
    output_post = []
    for posts in posts_data:
        if query.lower() in posts['content'].lower():
            output_post.append(posts)

    return output_post

def get_post_by_pk(posts_data: list, pk: int) -> dict:
    """
    Функция возвращает один пост по его идентификатору (PK)
    :param posts_data: Данные о размещенных на сайте постах из data.json -> list
    :param pk: Номер pk
    :return: пост, соответствующий PK
    """
    posts_by_pk = {}
    for post in posts_data:
        if pk == post['pk']:
            posts_by_pk = post

    return posts_by_pk