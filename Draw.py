#wayne w 2015
#draw webpage
import urllib.request, urllib.parse, urllib.error
import sys
#import and init pygame
import pygame
from pygame.locals import *
import random
import time

WIDTH = 1024 #640
HEIGHT = 1024 #480
MAGNITUDE = 7
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
# init
pygame.init() 
pygame.display.set_caption('Drawing a web page')
#create the screen
window = pygame.display.set_mode((WIDTH, HEIGHT)) 

#font = pygame.font.Font(None, 36)
# last param = color rgb
#text = font.render("dsfsdfsdfsdf", 1, (255, 255, 255))
#window.blit(text, (WIDTH- 200, 200)) # x,y


## URL Stuff
opener = urllib.request.FancyURLopener({})
URL = opener.open("http://192.168.0.1")
page = str(URL.read())
print (type(page))
print("###################################")
#print len(page)

alpha_coord = []
# change magnitude of numbers here
for i in range(len(page)):
	#if page[i] == '\n' or page[i] == '\t':
	#	print "page formatting passed"
	alpha_coord.append(ord(page[i]) * MAGNITUDE)

#print alpha_coord

# if not even, append newline number equiv
# [want lists of 4 items]
if len(alpha_coord) % 2 != 0:
	alpha_coord.append(ord('\n'))


# lists will also look different as web page changes [time, date, title etc]
drawing_coord = []
# loop with step of 4, new list [step:step no]
# if step + 4 == len(alpha) list[step:]
x = 0

for i in range(0, int( len(alpha_coord) / 4 ) ):
	drawing_coord.append(alpha_coord[x:x+4])
	x+=4

def draw_line(plot_list):
	# single line  
	#pygame.draw.line(window, (255, 255, 255), (plot_list[0], plot_list[1]), (plot_list[2], plot_list[3])) 
	pygame.draw.aaline(window, (255, 255, 255), (plot_list[0], plot_list[1]), (plot_list[2], plot_list[3]), blend=1)
	
	#draw it to the screen
	pygame.display.flip()
 
def draw_connected_lines(points):
	# joined lines
	pygame.draw.lines(window, WHITE, False, points, 1)

	#draw it to the screen
	pygame.display.flip()
	pygame.image.save(window, "_image.JPEG")

def one_line_begin():
	
	for i in range(len(drawing_coord)): 
		#print drawing_coord[i]
		draw_line(drawing_coord[i])
		
def joined_lines_begin():
	x = 0
	plot_joined_list = []
	#   
	for i in range(int(len(alpha_coord) / 2)):
		#print alpha_coord[x:x+2]
		plot_joined_list.append(alpha_coord[x:x+2])
		x +=2
	draw_connected_lines(plot_joined_list)	

#
joined_lines_begin()
print("done")

