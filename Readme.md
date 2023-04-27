# Twitter Clone
## Description
This is a Twitter clone built using Django. It allows users to post tweets, edit their profiles, add hashtags, include images in their posts, like posts, and follow other users.

## Features
### User Registration and Authentication
- Users can register for an account and log in to the platform.
- Passwords are securely stored using hashing techniques.
- User authentication is implemented to restrict access to certain features.
### User Profile
- Users can edit their profile information, including their name, bio, and profile picture.
- Profile pictures can be uploaded and stored in the system.
### Posting Tweets
- Users can create new tweets and share their thoughts.
- Tweets can contain text and images.
- Images are stored and displayed alongside the tweet.
- Tweets can be edited or deleted by the user who created them.
### Hashtags
- Users can add hashtags to their tweets to categorize them.
- Clicking on a hashtag shows a list of all tweets containing that hashtag.
- Hashtags are searchable and clickable within tweets.
### Like Posts
- Users can like posts to show their appreciation or interest.

## Installation
1. Clone the repository: `https://github.com/MubarekHussen/tweet_clone_with_django`
2. Create a virtual environment and activate it.
3. Install the required packages: `pip install -r requirements.txt`
4. Migrate the database: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Usage
Once the server is running, open your browser and go to `http://127.0.0.1:8000/` to access the application. You can register a new user account, then login to post tweets, edit your profile, and like and follow other users.
