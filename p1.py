import cv2
import os
from datetime import datetime, timedelta
import yt_dlp
import time

# Define constants
capture_duration = 2 * 60  # 2 minutes in seconds
fps = 15  # Frames per second
save_folder = "last_2_minutes_frames"
output_video = "last_2_minutes.mp4"  # Output video file name
max_retries = 5  # Max retries for stability
retry_delay = 10  # Wait time between retries in seconds

# Ensure the save folder exists
os.makedirs(save_folder, exist_ok=True)

# Define the YouTube video URL
youtube_url = "https://www.youtube.com/watch?v=II_m28Bm-iM"

# Function to get the direct video URL using yt-dlp
def get_video_url(youtube_url):
    ydl_opts = {
        'format': 'best[height<=480]',  # Limit resolution to 480p to save memory
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_url, download=False)
        return info_dict.get("url", None)

# Initialize video stream
video_url = get_video_url(youtube_url)
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

print("Streaming video from YouTube for 2 minutes. Press 'q' to quit.")

try:
    # Start timer for 2-minute capture
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=capture_duration)
    
    # Initialize video writer
    height, width = 360, 640  # Set target resolution
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    retry_count = 0
    while datetime.now() < end_time:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Handle frame read failure
        if not ret:
            print(f"Error: Can't receive frame. Retrying in {retry_delay} seconds... (Attempt {retry_count + 1}/{max_retries})")
            time.sleep(retry_delay)
            retry_count += 1
            
            # Refresh the video URL if retries reach a threshold
            if retry_count >= max_retries:
                print("Max retries reached. Exiting ...")
                break
            
            # Reinitialize video capture
            video_url = get_video_url(youtube_url)
            cap.release()
            cap = cv2.VideoCapture(video_url)
            continue

        retry_count = 0  # Reset retry count on successful frame capture
        
        # Downscale the frame to reduce memory usage
        frame = cv2.resize(frame, (width, height))

        # Write frame to video file
        out.write(frame)

        # Save each frame as an image
        timestamp = datetime.now()
        filename = os.path.join(save_folder, f"{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame)
        
        # Display the frame
        cv2.imshow('YouTube Stream - Last 2 Minutes', frame)
        
        # Check if 'q' key is pressed to break the loop early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exit requested by user.")
            break

finally:
    # Cleanup
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("2-minute video stream capture ended.")
