thonimport json
import requests
from instagram_parser import InstagramParser
from outputs.exporters import export_to_json

def run_scraper(post_url):
    print(f"Starting to scrape post: {post_url}")
    parser = InstagramParser(post_url)
    data = parser.get_engagement_data()

    # Export the scraped data to a JSON file
    export_to_json(data, 'output.json')

if __name__ == "__main__":
    post_url = 'https://www.instagram.com/p/DJHhRQzMLWD/'  # Example post URL
    run_scraper(post_url)