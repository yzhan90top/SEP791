import whisper
import os
import warnings
import re

warnings.filterwarnings("ignore")

# Make sure ffmpeg is accessible (required by whisper)
os.environ["PATH"] += os.pathsep + "/usr/local/bin"

# Load the Whisper model (you can change "base" to "small", "medium", etc.)
model = whisper.load_model("base")

# 🔽 Replace the following path with the full path to your recorded audio file (.wav format)
# For example: "/Users/yourname/Desktop/recorded.wav" on macOS
#              or "C:\\Users\\yourname\\recorded.wav" on Windows
result = model.transcribe("../recorded.wav", language="en")

cleaned = re.sub(r'[^\x00-\x7F]+', '', result["text"])

# Output the cleaned transcription
print(cleaned)