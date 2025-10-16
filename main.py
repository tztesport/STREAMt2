import os
import subprocess
import time

YOUTUBE_URL = "https://youtu.be/TMSAwKCP7AY?si=7Lu1XQjM5dUJ3dt0"
STREAM_KEY = os.getenv("STREAM_KEY")
STREAM_URL = f"rtmp://live.twitch.tv/app/{STREAM_KEY}"

def stream_loop():
    while True:
        print("🎥 Lancement du stream depuis YouTube...")
        cmd = (
            f"yt-dlp -f best -o - {YOUTUBE_URL} | "
            f"ffmpeg -re -i pipe:0 -c:v libx264 -preset veryfast -b:v 2500k "
            f"-c:a aac -b:a 160k -f flv {STREAM_URL}"
        )
        subprocess.run(cmd, shell=True)
        print("⚠️ Flux interrompu, redémarrage dans 5 secondes...")
        time.sleep(5)

if __name__ == '__main__':
    stream_loop()
