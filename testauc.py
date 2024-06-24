


import os
from playsound import playsound

audio_file_path = r'D:\Desktop files\AIVA_MAIN\AIVA_MAIN\quarter spin flac.mp3'
if os.path.exists(audio_file_path):
    playsound(audio_file_path)
else:
    print("Audio file does not exist at:", audio_file_path)
