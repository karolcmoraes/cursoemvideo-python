# Desafio 21
# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
# Aula 8

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()