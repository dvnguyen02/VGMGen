import requests
from bs4 import BeautifulSoup
import os 
import time
from urllib.parse import urljoin, unquote
import re

class VideoGameMusicDownloader:
    def __init__(self, base_url = "https://www.vgmusic.com"):
        self.base_url = base_url
        self.session = requests.Session()
        # Add headers to minmic browser behavior
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_console_links(self):
        """Get links to all console sections"""
        try:
            response = self.session.get(f"{self.base_url}/music/")
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all console links in the navigation
            console_links = []
            for link in soup.find_all('a'):
                href = link.get('href', '')
                if 'music/' in href and href != 'music/':
                    full_url = urljoin(self.base_url, href)
                    console_links.append(full_url)
            
            return console_links
        except Exception as e:
            print(f"Error getting console links: {str(e)}")
            return []

    def get_midi_links(self, console_url):
        """Get all MIDI file links from a console page"""
        try:
            response = self.session.get(console_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            midi_links = []
            for link in soup.find_all('a'):
                href = link.get('href', '')
                if href.lower().endswith('.mid'):
                    full_url = urljoin(console_url, href)
                    midi_links.append(full_url)
            
            return midi_links
        except Exception as e:
            print(f"Error getting MIDI links from {console_url}: {str(e)}")
            return []

    def download_midi(self, midi_url, output_dir):
        """Download a single MIDI file"""
        try:
            # Extract filename from URL and clean it
            filename = unquote(midi_url.split('/')[-1])
            # Remove invalid characters from filename
            filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
            
            # Create console-specific subdirectory
            console_name = midi_url.split('/')[-2]
            console_dir = os.path.join(output_dir, console_name)
            os.makedirs(console_dir, exist_ok=True)
            
            file_path = os.path.join(console_dir, filename)
            
            # Skip if file already exists
            if os.path.exists(file_path):
                return True
            
            # Download the file
            response = self.session.get(midi_url)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                return True
            else:
                print(f"Failed to download {filename}: Status code {response.status_code}")
                return False
                
        except Exception as e:
            print(f"Error downloading {midi_url}: {str(e)}")
            return False

    def download_all(self, output_dir="vgmusic_midis"):
        """Download all MIDI files from all consoles"""
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Get all console pages
        console_links = self.get_console_links()
        print(f"Found {len(console_links)} console sections")
        
        total_downloaded = 0
        failed_downloads = []
        
        # Process each console
        for console_url in console_links:
            console_name = console_url.split('/')[-2]
            print(f"\nProcessing {console_name}...")
            
            # Get all MIDI links for this console
            midi_links = self.get_midi_links(console_url)
            print(f"Found {len(midi_links)} MIDI files")
            
            # Download each MIDI file
            for midi_url in midi_links:
                # Add delay to be nice to the server
                time.sleep(1)
                if self.download_midi(midi_url, output_dir):
                    total_downloaded += 1
                else:
                    failed_downloads.append(midi_url)
        
        # Print summary
        print("\nDownload Summary:")
        print(f"Total files downloaded: {total_downloaded}")
        print(f"Failed downloads: {len(failed_downloads)}")
        if failed_downloads:
            print("\nFailed URLs:")
            for url in failed_downloads:
                print(url)

def main():
    # Create downloader instance
    downloader = VideoGameMusicDownloader()
    
    # Set output directory
    output_dir = "vgmusic_dataset"
    
    # Start download with progress tracking
    print("Starting VGMusic MIDI download...")
    downloader.download_all(output_dir)
    print("\nDownload process completed!")

if __name__ == "__main__":
    main()