#!/usr/bin/python3
from datetime import datetime
import praw
from Programs.log_file import archive_log_file, overwrite_log_file, write_to_log_file
from Programs.reddit_text_files import create_set


reddit_keywords_file_path = 'Files/reddit_keywords.txt'
reddit_flairs_file_path = 'Files/reddit_flairs.txt'
reddit_urls_file_path = 'Files/reddit_urls.txt'

start_time = datetime.now()

overwrite_log_file()

# Initialize the application with user specific credentials from Reddit
reddit = praw.Reddit(client_id="ADD_CLIENT_ID_HERE",
                     client_secret="ADD_CLIENT_SECRET_HERE",
                     user_agent="ADD_USER_AGENT_HERE",
                     password='ADD_PASSWORD_HERE',
                     username='ADD_USERNAME_HERE')

reddit_keywords = create_set(reddit_keywords_file_path)
reddit_flairs = create_set(reddit_flairs_file_path)
reddit_urls = create_set(reddit_urls_file_path)

hidden_dict = {'Keyword': {}, 'Flair': {}, 'Url': {}}

user_subreddits = list(reddit.user.subreddits())
for i in range(len(user_subreddits)):
    subreddit_name = user_subreddits[i]

    subreddit = reddit.subreddit(str(subreddit_name))
    for submission in subreddit.hot(limit=40):
        post_title = str(submission.title).replace("'", '’')
        post_url = str(submission.url).replace("'", '’').split('/')[2]
        post_flair = str(submission.link_flair_text).replace("'", '’')
        post_id = submission.id

        for keyword in reddit_keywords:
            if keyword in post_title:
                hide_post = reddit.submission(id=str(post_id))
                hide_post.hide()

                if keyword not in hidden_dict['Keyword']:
                    hidden_dict['Keyword'][keyword] = 1
                else:
                    hidden_dict['Keyword'][keyword] += 1

        for flair in reddit_flairs:
            if flair in post_flair:
                hide_post = reddit.submission(id=str(post_id))
                hide_post.hide()

                if flair not in hidden_dict['Flair']:
                    hidden_dict['Flair'][flair] = 1
                else:
                    hidden_dict['Flair'][flair] += 1

        for url in reddit_urls:
            if url in post_url:
                hide_post = reddit.submission(id=str(post_id))
                hide_post.hide()

                if url not in hidden_dict['Url']:
                    hidden_dict['Url'][url] = 1
                else:
                    hidden_dict['Url'][url] += 1

for key in hidden_dict:
    for hidden_item in hidden_dict[key]:
        if hidden_dict[key][hidden_item] == 1:
            write_to_log_file(title=f'HIDDEN {key.upper()}',
                              message=f'"{hidden_item}" was found in 1 post.')
        else:
            write_to_log_file(title=f'HIDDEN {key.upper()}',
                              message=f'"{hidden_item}" was found in {hidden_dict[key][hidden_item]} posts.')

execution_time = str(datetime.now() - start_time)

write_to_log_file(title='PROGRAM COMPLETED',
                  message='/.../RUN.py has completed with an execution time of ' +
                          execution_time + '.')

archive_log_file()
