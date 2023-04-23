# Project Description

This project is a set of Python scripts that can be used to download music from Spotify and YouTube and then join them together into a single MP3 file. The following instructions will guide you through the installation process and how to use each of the scripts.

Installation

To install the required libraries, run the following command in your terminal:

```python
pip install -r requirements.txt
```

This will install all the necessary libraries for the project.

Spotify Downloader

To use the Spotify Downloader, run the following command in your terminal:

```python
python3 spotify_Downloader.py
```

This script requires a Spotify Client ID and Secret Key to work. If you have not done this before, you can follow these steps:

Go to [Spotify Dev](https://developer.spotify.com/dashboard/applications)
Sign in and create an app (if you don't have one already)
Copy the Client ID and Secret Key from inside the app
For Linux users, you can export these credentials using the following commands in your terminal:

```bash
export SPOTIPY_CLIENT_ID='Your Spotify Client Id'
export SPOTIPY_CLIENT_SECRET='Your Spotify Secret key'
```
> Please do not share your credentials with anyone.

Youtube MP3 Downloader

To use the YouTube MP3 Downloader, run the following command in your terminal:

```python
python3 youtube_audio_downloader.py
```

This script will prompt you to enter the YouTube URL for the video you want to download. Once the download is complete, the audio will be automatically converted to MP3 format.

MP3 Joiner

To use the MP3 Joiner, run the following command in your terminal:

```python3
python3 mp3_Joiner.py
```

This script will prompt you to enter the file paths for the MP3 files you want to join together. You can enter either relative or absolute paths.

Please note that the MP3 Joiner script requires the ffmpeg library to be installed on your system.

Conclusion

This project provides a convenient way to download and join music from Spotify and YouTube. By following these instructions, you should be able to use each of the scripts to download and combine your favorite tracks into a single MP3 file.
