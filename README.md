# Last5MinsOfStream
ToSaveLast5MinsOfStream and save the frames

Stream Recorder with Last 5-Minute Clip Saving and Frame Capture
This project provides functionality to save the last 5 minutes of a live stream and continuously save live stream frames. It also converts the audio from the last 5-minute clip into an MP3 file. It’s ideal for stream monitoring or creating clips from ongoing streams.

Features
Continuous Stream Monitoring:

Captures and monitors live video and audio streams in real-time.
Processes the stream data for further operations.
Save Last 5 Minutes of Stream:

Continuously buffers the last 5 minutes of the live stream.
Saves the buffered video segment when triggered.
Frame Extraction:

Extracts and saves frames from the live video stream at regular intervals.
Useful for visual snapshots or analysis.
Audio Conversion to MP3:

Extracts the audio from the saved 5-minute video clip.
Converts the extracted audio to an MP3 format for lightweight and portable use.
How It Works
Stream Handling:

The program initializes a buffer to keep a rolling record of the last 5 minutes of the stream using a circular buffer mechanism.
Saving the Last 5 Minutes:

When triggered (e.g., by user input or a specific event), the buffered content is written to a video file.
This operation ensures no performance hit on the live streaming functionality.
Frame Capture:

Frames are continuously extracted from the stream and saved as image files at regular intervals.
File naming conventions ensure chronological order for easy analysis.
Audio Extraction and Conversion:

After saving the 5-minute video, the audio is extracted using a media processing library (e.g., FFmpeg).
The audio is encoded into an MP3 format, making it portable and compatible with most media players.
Prerequisites
Python 3.x: Ensure Python is installed.
Required Libraries:
opencv-python: For video processing.
numpy: For efficient buffer handling.
pydub or ffmpeg-python: For audio extraction and MP3 conversion.
(Optional) Additional libraries depending on stream source, such as requests for online streams.
