from flask import Flask, request, render_template, redirect
import functions

app = Flask('my_inst')

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

    # берем данные из аргумента 's'
    s = request.args.get('s')
    if s is None:
        return 'Введите параметр для поиска'
    s = s.lower()

    # помещаем найденный пост в match(list)
    match = functions.search_for_posts(posts_data, s)
    # post - обновленный список post_data с указанием количества комментов
    posts = functions.comments_count(match, comments_data)
    if len(match):
        quantity = len(match)
        return render_template('search.html', post=posts, s=s, quantity=quantity)
    return 'Ничего не найдено'


app.run()
