import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import yt_dlp
import time

class YouTubePlaylistDownloader:
    def __init__(self, playlist_url, download_directory='C:\\Users\\Admin\\Desktop\\youtube'):
        self.playlist_url = playlist_url
        self.video_links = []
        self.download_directory = download_directory

    def setup_driver(self):
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)

    def get_video_links(self):
        driver = self.setup_driver()
        driver.get(self.playlist_url)
        
        # Allow time for the page to load
        time.sleep(5)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        for a in soup.find_all('a', href=True):
            if '/watch' in a['href']:
                self.video_links.append('https://www.youtube.com' + a['href'])

    def download_videos(self):
        ydl_opts = {
            'outtmpl': os.path.join(self.download_directory, '%(title)s.%(ext)s'),  # Save as title.extension
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(self.video_links)

    def set_download_path(self):
        os.makedirs(self.download_directory, exist_ok=True)  # Ensure the directory exists

    def run(self):
        self.set_download_path()
        self.get_video_links()
        self.download_videos()

if __name__ == "__main__":
    downloader = YouTubePlaylistDownloader(input())
    downloader.run()
