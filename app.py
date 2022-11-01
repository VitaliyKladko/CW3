from flask import Flask, request, render_template, jsonify
import logging
import functions
from logger import logger_config


app = Flask(__name__)

api_logger = logging.getLogger('api_logger')
logger_config()


@app.route('/', methods=['GET'])
def main_page():
    posts_data = functions.open_json('data/posts.json')
    comments_data = functions.open_json('data/comments.json')
    bookmarks = functions.open_json('data/bookmarks.json')

    posts_data = functions.string_crop(posts_data)
    posts_data = functions.comments_count(posts_data, comments_data)

    bookmarks_quantity = len(bookmarks)

    return render_template('index.html', posts=posts_data, bookmarks_quantity=bookmarks_quantity)


@app.route('/post/<postid>', methods=['GET'])
def post_page(postid):
    post_data = functions.open_json('data/posts.json')
    comments_data = functions.open_json('data/comments.json')

    # приводим postid к int, так как он str
    postid = int(postid)

    # берем нужный пост из всех постов с помощью функции get_post()
    output_post = functions.get_post_by_pk(post_data, postid)
    tags = functions.get_tags(output_post)

    # достаем комменты по посту и ловим исключение если такого поста нет в списке
    output_comments = functions.get_comments_by_post_id(comments_data, postid)

    # комментарии_количество
    comments_quantity = len(output_comments)

    # Рендрим пост
    return render_template('post.html', post=output_post, comments=output_comments, quantity=comments_quantity,
                           tags=tags)


@app.route('/search/', methods=['GET'])
def search_page():
    posts_data = functions.open_json('data/posts.json')
    comments_data = functions.open_json('data/comments.json')

    s = request.args.get('s')

    if s is None:
        return 'Вы ничего не ввели'

    s = s.lower()

    # помещаем найденный пост в match(list)
    match = functions.search_for_posts(posts_data, s)
    # post - обновленный список post_data с указанием количества комментов
    posts = functions.comments_count(match, comments_data)
    posts = functions.string_crop(posts)
    if len(match):
        quantity = len(match)
        return render_template('search.html', post=posts, s=s, quantity=quantity)
    return 'Ничего не найдено'


@app.route('/users/<username>', methods=['GET'])
def user_page(username):
    posts_data = functions.open_json('data/posts.json')
    comments_data = functions.open_json('data/comments.json')

    # находим посты человека и колл-во комментариев к ним
    math = functions.get_posts_by_user(posts_data, username)
    posts = functions.comments_count(math, comments_data)
    posts = functions.string_crop(posts)

    return render_template('user-feed.html', posts=posts, name=username)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500


@app.route('/api/posts/')
def json_all_posts():
    posts_data = functions.open_json('data/posts.json')
    api_logger.debug('Запрос /api/posts')
    return jsonify(posts_data)


@app.route('/api/posts/<post_id>')
def json_post(post_id):
    posts_data = functions.open_json('data/posts.json')
    post_num = int(post_id)
    post = functions.get_post_by_pk(posts_data, post_num)
    api_logger.debug(f'Запрос /api/posts/{post_id}')
    return jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)
