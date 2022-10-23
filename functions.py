import json

def open_json(file) -> list:
    """
    Функция производит чтение данных из .json файла, загружает все посты
    :param file: Файл .json, который необходимо прочитать
    :return: данные из файла .json (список словарей)
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
    is_exists = False
    output_post = []
    for post in posts_data:
        if user_name == post['poster_name']:
            is_exists = True
            output_post.append(post)

    if not is_exists:
        raise ValueError

    return output_post

def get_comments_by_post_id(comment_data: list, post_id: int) -> list:
    """
    Функция возвращает комментарии определенного поста по его ID
    :param comment_data: Список словарей комментариев -> list
    :param post_id: номер поста (его ID) -> int
    :return: Список словарей
    """
    # все комменты к посту
    output_comments = []
    is_exists = False
    for comment in comment_data:
        if post_id == comment['post_id']:
            is_exists = True
            output_comments.append(comment)

    if not is_exists:
        raise ValueError

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


def string_crop(post_data) -> list:
    """
    Функция производит сокращение строки до 50 символов
    :param post_data: Данные о постах, в которых необходимо сократить строку
    :return: Обнавленный post-data
    """
    for post in post_data:
        post['content'] = post['content'][:50]

    return post_data


def comments_count(post_data, comments_data) -> list:
    """
    Функция производит подсчет количества комментариев к постам
    :param post_data: Данные о размещенных на сайте постах из posts.json
    :param comments_data: Данные о комментариях ко всем постам из файла comments.json
    :return: Обновленный список post_data с количеством комментариев для каждого поста
    """
    comments_math = []
    for post in post_data:
        for comment in comments_data:
            if comment['post_id'] == post['pk']:
                comments_math.append(post['pk'])
            post['comments'] = comments_math.count(post['pk'])

    return post_data


def get_tags(post) -> list:
    """
    Функция вытаскивает теги
    :param post: наш пост
    :return: list - список тегов
    """
    tags = []
    text = post['content'].split(' ')
    for word in text:
        if '#' in word:
            tag = word.replace('#', '')
            tags.append(tag)

    return tags