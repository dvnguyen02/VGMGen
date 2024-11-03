# VGMGen

![RNNs Structure](https://magenta.tensorflow.org/2016/06/10/recurrent-neural-network-generation-tutorial)

After learning about RNNs, LSTMs, and GRUs from DeepLearning.AI, I was inspired to start this project to deepen my understanding of these concepts. This project focuses on generating video game music using Recurrent Neural Networks (RNNs). Currently, it includes tools for scraping MIDI files from VGMusic.com to use as training data.

![Audio Wave](https://github.com/dvnguyen02/VGMGen/blob/master/images/audio_wave.jpg?raw=true)


## Current Features

### Data Downloader:
- Scrapes MIDI files from VGMusic.com
- Includes delay between downloads to be server-friendly

### Project Structure
```
project/
├── vgmusic_dataset/     # Downloaded MIDI files
│   ├── nintendo/
│   ├── sega/
│   └── ...
├── data_downloader.py           # MIDI file scraping script
└── README.md            
```

## Usage

### MIDI VGM Downloader

```python
# Create downloader instance
downloader = VideoGameMusicDownloader()

# Set output directory
output_dir = "vgmusic_dataset"

# Start downloading
downloader.download_all(output_dir)

# To run this code 
python data_downloader.py # It will automatically download all the audio files from the size, or if you want you could modify to download from a specific console from the code.
```


Methods:
- `get_console_links()`: Retrieves links to all console sections
- `get_midi_links(console_url)`: Gets all MIDI file links from a specific console page
- `download_midi(midi_url, output_dir)`: Downloads a single MIDI file
- `download_all(output_dir)`: Downloads all MIDI files from all consoles


## Contributing

This project is currently under development. Contributions, suggestions, and feedback are welcome!

## Notes

- The scraper includes a 1-second delay between downloads to avoid overwhelming the server

