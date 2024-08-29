from youtube_transcript_api import YouTubeTranscriptApi
import os

srt = YouTubeTranscriptApi.get_transcript("jzD_yyEcp0M")

text = ""

with open("file.txt", "w") as file:
    for i in srt:
       print(i['text'])
       text += i['text'] + "\n"
    file.write(text)   

os.startfile("file.txt")    