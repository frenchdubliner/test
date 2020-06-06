#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:11:35 2020

@author: olivier
"""


import pygame

#Intialisation of pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Olivier the unicorn")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('swimming-pool.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))
    
#Game loop
running = True
try:
    while running:
        
        #RGB = Red, Green, Blue
        screen.fill((3,232,252))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #if keystroke is pressed check whether it is right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change =-0.3
                if event.key == pygame.K_RIGHT:
                    playerX_change =0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   playerX_change =0
        playerX += playerX_change
        player(playerX,playerY)
        pygame.display.update()
        
    pygame.quit()
except SystemExit:
    pygame.quit()