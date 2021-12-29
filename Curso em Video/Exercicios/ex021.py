# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygama import mixer

mixer.init()
mixer.music.load(C:\Users\Vincy\Music/a77e27df010f6a271024c3a39143ae4a.mp3)
mixer.music.play()
