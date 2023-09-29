# reddit-content-filter
A Reddit content filtering program for mobile devices connected to a Raspberry Pi via SSH, enabling users to hide unwanted posts with ease and gain greater control over their Reddit experience through automated Reddit API interactions.

**Required Packages:** praw // requests

**Additional Requirements:** Raspberry Pi (or another available computer) // Siri Shortcuts

# Prerequisites
Before you can use this program, make sure you have the following prerequisites in place:
1. **Python 3:** This program is written in Python 3.
2. **PRAW (Python Reddit API Wrapper):** You'll need to install PRAW. You can install it using pip with the following command: *pip install praw*
3. **Reddit API Credentials:** You need to create a Reddit application and obtain the following credentials:
   - 'client_id': Your Reddit API client ID.
   - 'client_secret': Your Reddit API client secret.
   - 'user_agent': A unique user agent string to identify your program.
4. **Reddit Account Credentials:** You'll need the Reddit username and password for the account that will be used to interact with Reddit.
