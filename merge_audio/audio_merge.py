from pytube import YouTube
from pydub import AudioSegment

def downloadAudio(brainWaveUrl: str, audioBookUrl: str) -> None:
    """
    下载音频

    如果太慢，就放到 colab 上跑，再下载下来
    """
    brainWave = YouTube(brainWaveUrl)
    audioBook = YouTube(audioBookUrl)

    brainWaveStream = brainWave.streams.get_audio_only()
    brainWaveStream.download(filename="brainWave")

    audioBookStream = audioBook.streams.get_audio_only()
    audioBookStream.download(filename="audioBook")

def mergeAudio(
    brainWaveUrl: str = "brainWave.mp4", audioBookUrl: str = "audioBook.mp4"
    ) -> None:
    """对两个音频进行合并"""
    brainWave = AudioSegment.from_file(brainWaveUrl, format="mp4")
    audioBook = AudioSegment.from_file(audioBookUrl, format="mp4")

    print("Length of BrainWave: ", len(brainWave))
    print("Length of AudioBook: ", len(audioBook))

    output = audioBook.overlay(brainWave)
    output.export("output.mp3", format="mp3")
    print("Length of Output: ", len(output))

if __name__ == "__main__":
    brainWaveUrl = 'https://www.youtube.com/watch?v=cTM1YFg8h00&ab_channel=BrainwaveMusic'
    audioBookUrl = 'https://www.youtube.com/watch?v=MEL2C2Q9Hik&t=1164s&ab_channel=LeonardJohnson'
    downloadAudio(brainWaveUrl, audioBookUrl)
    mergeAudio()