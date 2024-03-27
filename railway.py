# We are making a software for the railway annoucement in india - English version
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    """Function to convert text to speech"""
    mytext = str(text)
    language = "en"
    myobj = gTTS(text= mytext,lang=language,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    """Function to merge the small audio files"""
    combined = AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    """Function to generate the base on which the announcement is to be made"""
    # May I have attention
    pass
    audio = AudioSegment.from_mp3('media/railway.mp3')
    start = 15000
    finish = 19000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format="mp3")

    # From
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 23000
    finish = 23700
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_english.mp3", format="mp3")

    # via
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 25000
    finish = 25550
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format="mp3")

    # is arriving on platform number
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 27000
    finish = 29400
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format="mp3")

    # end tone
    audio = AudioSegment.from_mp3('railway.mp3')
    start = 15000
    finish = 16600
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format="mp3")


def generateAnnoucement(filename):
    """Function to generate annoucement mp3 as a whole"""
    df = pd.read_excel(filename)
    for index,item in df.iterrows():
        textToSpeech(item['train_no'] +" " + item['train_name'],"2_english.mp3")
        textToSpeech(item['from'],"4_english.mp3")
        textToSpeech(item['via'],"6_english.mp3")
        textToSpeech(item['platform'],"8_english.mp3")
        audios = [f"{i}_english.mp3" for i in range(1,10)]
        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")


if __name__ == '__main__':
    print("Firstly generating skeleton")
    generateSkeleton()
    print("Into generating announcement")
    generateAnnoucement("announce_hindi.xlsx")
