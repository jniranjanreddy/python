# posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]


# first_post = posts[0]
# first_author_username = posts[0]['author']['username']

# second_post_body = posts[1]
# second_author_username = posts[1]['author']['username']
# second_author_username = posts[1]['author']['username'] = "niru"

# # print(first_post)
# # print(first_author_username)

# print(second_post_body)
# print(second_author_username)

posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]


# def update_usernames(posts):
#     for post in posts:
#         # Access the 'username' in the 'author' dictionary and update it
#         post['author']['username'] = post['author']['username'] + 'Updated'

# # Call the function
# update_usernames(posts)

# for post in posts:
#     print(post)

for i in range(1,3):
    for post in posts:
            post['author']['username'] = post['author']['username'] + i