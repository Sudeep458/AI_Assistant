import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class News:
    def __init__(self):
        self.api_key = os.getenv('NEWS_API_KEY')  # Get API key from environment variable
        self.url = 'https://newsapi.org/v2/top-headlines'

    def get_top_news(self, country='us'):
        """Fetch top news headlines from the specified country."""
        parameters = {
            'country': country,
            'apiKey': self.api_key
        }
        response = requests.get(self.url, params=parameters)
        
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            return articles
        else:
            print("Failed to fetch news:", response.status_code)
            return []

    def create_news_html(self, articles):
        """Create an HTML file to display the fetched news articles."""
        html_content = "<html><head><title>Top News</title></head><body>"
        html_content += "<h1>Top News Headlines</h1>"
        
        if not articles:
            html_content += "<p>No news articles found.</p>"
        else:
            for article in articles:
                title = article.get('title')
                description = article.get('description')
                url = article.get('url')
                html_content += f"<h2>{title}</h2><p>{description}</p><a href='{url}' target='_blank'>Read more</a><hr>"
        
        html_content += "</body></html>"
        
        # Write the HTML content to a file
        with open("top_news.html", "w") as file:
            file.write(html_content)