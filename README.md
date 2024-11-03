# MIDI Music Generation Project

This project aims to generate video game music using Recurrent Neural Networks (RNN). Currently, it includes tools for scraping MIDI files from VGMusic.com 

## Current Features

### Web Scraping Tools
- Scrapes MIDI files from VGMusic.com
- Organizes files by console/system
- Includes delay between downloads to be server-friendly
- Handles network errors gracefully
- Skips existing files for resume capability
- Provides progress updates and download summary

### Project Structure
```
project/
├── vgmusic_dataset/     # Downloaded MIDI files
│   ├── nintendo/
│   ├── sega/
│   └── ...
├── scraper.py           # MIDI file scraping script
└── README.md            
```

## Usage

### MIDI File Scraper

```python
# Create downloader instance
downloader = VideoGameMusicDownloader()

# Set output directory
output_dir = "vgmusic_dataset"

# Start downloading
downloader.download_all(output_dir)
```

Optional: Add `--shutdown` flag to shutdown computer after completion
```bash
python scraper.py --shutdown
```

### Class Documentation

#### VideoGameMusicDownloader
Main class for handling MIDI file downloads.

Methods:
- `get_console_links()`: Retrieves links to all console sections
- `get_midi_links(console_url)`: Gets all MIDI file links from a specific console page
- `download_midi(midi_url, output_dir)`: Downloads a single MIDI file
- `download_all(output_dir)`: Downloads all MIDI files from all consoles


## Contributing

This project is currently under development. Contributions, suggestions, and feedback are welcome!

## Notes

- The scraper includes a 1-second delay between downloads to avoid overwhelming the server
- Failed downloads are logged for later retry
- Downloads are organized by console for easy navigation
- Existing files are skipped to allow for interrupted downloads to resume


