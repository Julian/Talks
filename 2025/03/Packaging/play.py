import pygame
pygame.init()
pygame.mixer.music.load("cashregister.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(60)
