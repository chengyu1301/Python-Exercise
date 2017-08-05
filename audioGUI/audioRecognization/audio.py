import wave
from pyaudio import PyAudio, paInt16
import urllib, urllib.request
import pycurl
import json

NUM_OF_SAMPLES = 2000
TIME = 2 # Time for buffer

frameRate = 16000
channels = 1
sampleWidth = 2 # 2 bytes
myJWT = ''


"""Save the wave file"""
def saveWaveFile(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampleWidth)
    wf.setframerate(frameRate)
    wf.writeframes(b''.join(data))
    wf.close()
    
"""Record the audio"""
def recordAudio():
    pa = PyAudio()
    # Create a stream
    stream = pa.open(format = paInt16,
                     channels = 1,
                     rate = frameRate,
                     input = True,
                     frames_per_buffer = NUM_OF_SAMPLES)
    myBuffer = []
    count = 0
    while count < TIME*(frameRate/NUM_OF_SAMPLES):
        stringAudioData = stream.read(NUM_OF_SAMPLES)
        myBuffer.append(stringAudioData)
        count += 1
        print('.')
    saveWaveFile('01.wav', myBuffer)
    stream.close()

def readToken(buffer):
    global myJWT
    myJWT = str(buffer, 'utf-8')
    
    
    
def readResult(buffer):
    jsonData = json.loads(buffer)
    print(jsonData['DisplayText'])

def getToken():
    myKey = '252859b2183543b5ba4a2e6152a73e5a'
    authURL = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'

    httpHeader = ['Content-type: application/x-www-form-urlencoded',
                  'Content-Length: 0',
                  'Ocp-Apim-Subscription-Key: %s' % myKey]
    c = pycurl.Curl()
    c.setopt(pycurl.URL, authURL)
    c.setopt(c.HTTPHEADER, httpHeader)
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 60)
    c.setopt(c.TIMEOUT, 80)
    c.setopt(c.WRITEFUNCTION, readToken)
    c.perform()
    
def uploadToRec(filename):
    
    filePtr = wave.open(filename, 'rb')
    numberOfFrames = filePtr.getnframes()
    print('Sample Width: ', filePtr.getsampwidth())
    print('Frame rate: ', filePtr.getframerate())
    print('Channels: ', filePtr.getnchannels())
    fileLength = 2*numberOfFrames
    audioData = filePtr.readframes(numberOfFrames)
    
    comment = 'Authorization: Bearer '+myJWT
    serverURL = 'https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=pt-BR&locale=zh-TW&format=wav&requestid=64:b4:73:42:e3:78'
    httpHeader = [comment,
                  'Content-type: audio/wav; codec="audio/pcm"; samplerate=16000']
    c = pycurl.Curl()
    c.setopt(pycurl.URL, serverURL)
    c.setopt(c.HTTPHEADER, httpHeader)
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 60)
    c.setopt(c.TIMEOUT, 80)
    c.setopt(c.WRITEFUNCTION, readResult)
    c.setopt(c.POSTFIELDS, audioData)
    c.setopt(c.POSTFIELDSIZE, fileLength)
    c.perform()
    

recordAudio()
getToken()
uploadToRec('whatstheweatherlike.wav')
print('Done!')