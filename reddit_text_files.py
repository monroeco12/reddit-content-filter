#!/usr/bin/python3
def create_set(file_path):
    to_be_hidden_set = set()

    with open(file_path, 'r') as reddit_text_file:
        for line in reddit_text_file:
            reddit_text = line.replace("'", '’').replace('__', ' ').replace('\n', '')
            if reddit_text != '':
                to_be_hidden_set.add(reddit_text)

    return to_be_hidden_set
