from flask import Flask, request, render_template, redirect
import functions

app = Flask('my_inst')

@app.route('/')
def main_page():
    posts_data = functions.open_json('data/posts.json')
    comments_data = functions.open_json('data/comments.json')
    bookmarks = functions.open_json('data/bookmarks.json')

    posts_data = functions.string_crop(posts_data)
    posts_data = functions.comments_count(posts_data, comments_data)

    bookmarks_quantity = len(bookmarks)

    return render_template('index.html', posts=posts_data, bookmarks_quantity=bookmarks_quantity)

@app.route('/post/<postid>')
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

app.run()
