thonimport requests
from bs4 import BeautifulSoup

class InstagramParser:
    def __init__(self, post_url):
        self.post_url = post_url

    def get_engagement_data(self):
        print(f"Fetching data from: {self.post_url}")
        response = requests.get(self.post_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting relevant engagement data (mocked example)
        data = {
            "type": "comments",
            "link_post": self.post_url,
            "comment_like_count": 5,
            "created_at": 1626474444,
            "hashtags": ['#love', '#instagood'],
            "like_count": 250,
            "mentions": ['@user1'],
            "text": "🔥❤️🔥",
            "link_user": "https://www.instagram.com/user1",
            "user": {
                "full_name": "User One",
                "id": "123456789",
                "is_private": False,
                "is_verified": False,
                "profile_pic_url": "https://example.com/profile.jpg",
                "username": "user1"
            }
        }
        return data