# reddit-content-filter
A Reddit content filtering program for mobile devices connected to a Raspberry Pi via SSH, enabling users to hide unwanted posts with ease and gain greater control over their Reddit experience through automated Reddit API interactions.

**Required Package:** praw

**Additional Requirements:** Raspberry Pi (or another available computer) // Siri Shortcuts

# Prerequisites
Before you can use this program, make sure you have the following prerequisites in place:
1. **Python 3:** This program is written in Python 3. You can download and install it from the official [Python website](https://www.python.org/downloads/).
2. **praw:** The Python Reddit API Wrapper accesses Reddit's API. You can install it using pip with the following command: *pip install praw*
3. **Reddit API Credentials:** You need to create a Reddit application and obtain the following credentials:
   - 'client_id': Your Reddit API client ID.
   - 'client_secret': Your Reddit API client secret.
   - 'user_agent': A unique user agent string to identify your program.
4. **Reddit Account Credentials:** You'll need the Reddit username and password for the account that will be used to interact with Reddit.

# Configuration
Before running the program, you need to configure it by providing the necessary credentials. Here's how to do it:
1. Replace the placeholders in the **RUN.py** file with your Reddit API credentials:
   - 'client_id': Replace "ADD_CLIENT_ID_HERE" with your actual client ID.
   - 'client_secret': Replace "ADD_CLIENT_SECRET_HERE" with your actual client secret.
   - 'user_agent': Replace "ADD_USER_AGENT_HERE" with your unique user agent.
   - 'password': Replace "ADD_PASSWORD_HERE" with your Reddit account password.
   - 'username': Replace "ADD_USERNAME_HERE" with your Reddit username.

# Usage
The program can run automatically by using **cron** or other similar software. The following **cron** command will run the program every 20 minutes: **/20 * * * * /your/path/to/RUN.py*

The program will do the following:
1. Initialize a connection to Reddit using your credentials.
2. Read keywords, flairs, and URLs from text files.
3. Create a dictionary to store the counts of hidden posts based on keywords, flairs, and URLs.
4. Iterate through your subscribed subreddits and their *Hot* posts.
5. For each post, it checks if it matches any of the keywords, flairs, or URLs. If it does, the post is hidden, and the program updates the count in the dictionary.
6. After processing all posts, the program logs the counts of hidden posts in a log file along with the program's execution time.
7. Finally, it archives the log file.

To remotely update the keywords, flairs, and URLs text files from an Apple device, refer to the [Siri Shortcuts Workflow.md](https://github.com/monroeco12/reddit-content-filter/blob/main/Siri%20Shortcuts%20Workflow.md) file. The following video demonstrates the Siri Shortcut in action:

https://github.com/monroeco12/reddit-content-filter/assets/116775849/e454aa85-d1a4-4e96-ac2b-fb5de06140e3

# Logging
The program logs its actions and the counts of hidden posts in a log file located in the **Files** directory. The log entries include information about hidden keywords, flairs, and URLs, as well as the program's execution time.

# Notes
- The program hides posts automatically, so use it responsibly and ensure that it complies with Reddit's terms of service and subreddit rules.
- Make sure you keep your credentials and program files secure, as they contain sensitive information.
- You can adjust the submission limit value in the **RUN.py** file to control how many posts are processed in each subreddit's 'Hot' feed.
