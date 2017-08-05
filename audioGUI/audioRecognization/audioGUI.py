# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import wave
from pyaudio import PyAudio, paInt16
import urllib, urllib.request
import pycurl
import json
import threading
import time
import queue

import numpy as np
from datetime import datetime



from Ui_audioGUI import Ui_MainWindow


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        

    
    def run(self):
        print('Starting ', self.name, ' at ', time.ctime())
        self.res = self.func()
        print(self.name, ' finished at ', time.ctime())

class MainWindow(QMainWindow, Ui_MainWindow, threading.Thread):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        threading.Thread.__init__(self)
        #Variable declaration
        
       
        self.NUM_OF_SAMPLES = 2000
        self.TIME = 5 # Time for buffer
        self.frameRate = 16000
        self.channels = 1
        self.sampleWidth = 2 # 2 bytes
        self.saveFileIndex = 1
        self.LEVEL = 1000
        self.muteCountLimit = 50
        self.muteBegin = 0
        self.muteEnd = 1
        self.startFlag = 0
        self.wavQueue = queue.Queue(1024)
        self.setupUi(self)
        
    def run(self):
        print('Starting ', 'recordAudio', ' at ', time.ctime())
        self.res = self.recordAudio()
        print(self.name, ' finished at ', time.ctime())
        
        
        
    def writeQ(self, queue, data):
        queue.put(data, 1)
        
    def readQ(self, queue):
        val = queue.get(1)
        return val    
    
    """Save the wave file"""
    def saveWaveFile(self, filename, data):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampleWidth)
        wf.setframerate(self.frameRate)
        wf.writeframes(b''.join(data))
        wf.close()
        
    """Record the audio"""
    def recordAudio(self):
        
        while True:
            while self.startFlag == 1:
                
            
                pa = PyAudio()
                # Create a stream
                stream = pa.open(format = paInt16,
                                 channels = 1,
                                 rate = self.frameRate,
                                 input = True,
                                 frames_per_buffer = self.NUM_OF_SAMPLES)
                saveBuffer = []
                count = 0
                while count < self.TIME*(self.frameRate/self.NUM_OF_SAMPLES):
                    stringAudioData = stream.read(self.NUM_OF_SAMPLES)
                    audioData = np.fromstring(stringAudioData, dtype=np.short)
                    largestSampleCount = np.sum(audioData > self.LEVEL)
                    print(largestSampleCount)
                    
                    if largestSampleCount < self.muteCountLimit:
                        self.muteBegin = 1
                    else:
                        saveBuffer.append(stringAudioData)
                        self.muteBegin = 0
                        self.muteEnd = 1
                    
                    count += 1
                    if (self.muteEnd - self.muteBegin) > 9:
                        self.muteBegin = 0
                        self.muteEnd = 1
                        break
                    if self.muteBegin:
                        self.muteEnd += 1
                        
                saveBuffer = saveBuffer[:]
                if saveBuffer:
                    if self.saveFileIndex < 11:
                        pass
                    else:
                        self.saveFileIndex = 1
                    filename = str(self.saveFileIndex) + '.wav'
                    self.saveWaveFile(filename, saveBuffer)
                    self.writeQ(queue=self.wavQueue, data=filename)
                    self.saveFileIndex += 1
                    print(filename, ' saved')
                else:
                    print('File not saved')
                saveBuffer = []
                stream.close()

        
    def readToken(self, buffer):
        self.myJWT = str(buffer, 'utf-8')
        
        
        
    def readResult(self, buffer):
        jsonData = json.loads(buffer)
        print(jsonData)
        if 'DisplayText' in jsonData:
            print(jsonData['DisplayText'])
            self.textBrowser.append(jsonData['DisplayText'])

    def getToken(self):
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
        c.setopt(c.WRITEFUNCTION, self.readToken)
        try:
            c.perform()
        except Exception as e:
            print(e)
        time.sleep(0.3)
        
    def uploadToRec(self):

        self.getToken()
        while True:
            if self.wavQueue.qsize():
                filename = self.readQ(queue=self.wavQueue)
            else:
                continue
            filePtr = wave.open(filename, 'rb')
            numberOfFrames = filePtr.getnframes()
            print('Sample Width: ', filePtr.getsampwidth())
            print('Frame rate: ', filePtr.getframerate())
            print('Channels: ', filePtr.getnchannels())
            fileLength = 2*numberOfFrames
            audioData = filePtr.readframes(numberOfFrames)
            
            comment = 'Authorization: Bearer '+ self.myJWT
            print(comment)
            serverURL = 'https://speech.platform.bing.com/speech/recognition/interactive/cognitiveservices/v1?language=zh-TW&locale=zh-TW&format=wav&requestid=64:b4:73:42:e3:78'
            httpHeader = [comment,
                          'Content-type: audio/wav; codec="audio/pcm"; samplerate=16000']
            c = pycurl.Curl()
            c.setopt(pycurl.URL, serverURL)
            c.setopt(c.HTTPHEADER, httpHeader)
            c.setopt(c.POST, 1)
            c.setopt(c.CONNECTTIMEOUT, 60)
            c.setopt(c.TIMEOUT, 80)
            c.setopt(c.WRITEFUNCTION, self.readResult)
            c.setopt(c.POSTFIELDS, audioData)
            c.setopt(c.POSTFIELDSIZE, fileLength)
            c.perform()
            print('Done!')
        
        
    @pyqtSlot()
    def on_pushButtonStart_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('Start!')
        self.startFlag = 1
        self.labelStatus.setText('Status: Recording')
    
    @pyqtSlot()
    def on_pushButtonStop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.startFlag = 0
        self.labelStatus.setText('Status: Ready')
        print('Stop')
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.setDaemon(True)
    ui.start() 
    ui.show()
    uploadThread = MyThread(func = ui.uploadToRec, args = None, name = ui.uploadToRec.__name__)
    uploadThread.setDaemon(True)
    uploadThread.start()
    sys.exit(app.exec_())
