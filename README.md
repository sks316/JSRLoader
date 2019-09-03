# JSRLoader

JSRLoader is a downloader for the online radio station JetSetRadio.live. 

## How does it work?

You'd expect most online radio stations to play songs server-side and stream that to you via an M3U playlist file. With JetSetRadio.live, that isn't the case. JSRL streams the songs *directly to you* as MP3 files and keeps track of song names by storing them in a JS array. While this makes things easier server-side, it also means that we can download the songs *directly from JSRL* for free! To accomplish this, we use `urllib.request` to download the array, and `requests` to download the songs.

## Downloading and usage

Perform a `git clone`, navigate to the cloned directory, and run `pip install -r requirements.txt` to install everything JSRLoader needs to run.

Once everything is installed, run JSRLoader by running the following command:

Windows: ```
py jsrloader.py
```

Linux: ```
python3 jsrloader.py
```

Songs will be downloaded into `[Clone directory]/Downloaded music/[Station name]`.