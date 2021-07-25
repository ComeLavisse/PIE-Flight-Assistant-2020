# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:48:10 2021

@author: willi
"""

!pip install SpeechRecognition
!pip install pyaudio

import speech_recognition as sr
import time 
 
r  = sr.Recognizer()
with sr.Microphone() as source:
    print("Dites quelque chose")
    audio = r.listen(source)
try:
    tic = time.perf_counter()
    text = r.recognize_google(audio)
    toc = time.perf_counter()
    print('perfo = ', toc-tic, 's')
    print("You have said : " + text)
except sr.UnknownValueError:
    print("audio wasn't understood")
except sr.RequestError as e:
    print("Le service Google Speech API ne fonctionne plus" + format(e))