#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:11:35 2020

@author: olivier
"""


import pygame
import random

#Intialisation of pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.png')

#Title and Icon
pygame.display.set_caption("Olivier the unicorn")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('swimming-pool.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('sea.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x,y):
    screen.blit(playerImg,(x,y))
    
def enemy(x,y):
    screen.blit(enemyImg,(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
    
#Game loop
running = True
try:
    while running:
        
        #RGB = Red, Green, Blue
        screen.fill((3,232,252))
        #Display the background
        screen.blit(background,(0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #if keystroke is pressed check whether it is right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change =-5
                if event.key == pygame.K_RIGHT:
                    playerX_change =5
                if event.key == pygame.K_SPACE:
                    fire_bullet(playerX, bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   playerX_change =0
                   
        #checking for boundaries
        playerX += playerX_change
        
        if playerX <0:
            playerX=0
        elif playerX>736:
            playerX=736
            
        enemyX += enemyX_change
        
        if enemyX <0:
            enemyX_change = 4
            enemyY += enemyY_change
        elif enemyX>736:
            enemyX_change = -4
            enemyY += enemyY_change
            
        
        #Bullet movement
        if bullet_state is "fire":
            fire_bullet(playerX, bulletY)
            bulletY -= bulletY_change
            
        player(playerX,playerY)
        enemy(enemyX,enemyY)
        
        pygame.display.update()
        
    pygame.quit()
except SystemExit:
    pygame.quit()