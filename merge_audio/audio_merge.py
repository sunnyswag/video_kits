from pytube import YouTube

def downloadAudio(brainWaveUrl, audioBookUrl):

    # 如果太慢，就放到 colab 上跑
    brainWave = YouTube(brainWaveUrl)
    audioBook = YouTube(audioBookUrl)

    brainWaveStream = brainWave.streams.get_audio_only()
    brainWaveStream.download()

    audioBookStream = audioBook.streams.get_audio_only()
    audioBookStream.download()

if __name__ == "__main__":
    brainWaveUrl = 'https://www.youtube.com/watch?v=cTM1YFg8h00&ab_channel=BrainwaveMusic'
    audioBookUrl = 'https://www.youtube.com/watch?v=MEL2C2Q9Hik&t=1164s&ab_channel=LeonardJohnson'
    # downloadAudio(brainWaveUrl, audioBookUrl)