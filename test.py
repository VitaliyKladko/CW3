import functions

posts_data = functions.open_json('data/posts.json')
comments_data = functions.open_json('data/comments.json')


asd = functions.get_comments_by_post_id(comments_data, 1)
print(asd)


