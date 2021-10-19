# Import a library of functions called 'pygame'
from main_functions import *

# Initialize the game engine
pygame.init()

#call main rutine

ancho = int(input("ancho de la ventana: "))
alto = int(input("alto de la ventana: "))
size=[1300,600]
size[0]=ancho
size[1]=alto

titulo = input("titulo")
main2(size,titulo)
