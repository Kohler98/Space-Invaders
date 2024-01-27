import pygame   
from pygame import mixer
import random
from typing import final
import math
class Pantalla:
    def __init__(self,w,h) -> None:
       self.pantalla = pygame.display.set_mode((w,h))

    def mostrar_puntaje(self,x,y,puntaje):
        fuente = pygame.font.Font("freesansbold.ttf",32)
        texto = fuente.render(f"Puntaje : {puntaje}",True, (255,255,255))
        self.pantalla.blit(texto,(x,y))
    
    def sonido(self, sound):
        sonido_pantalla = mixer.Sound(sound)
        sonido_pantalla.play()
    
    def game_over(self):
        fuente_final = pygame.font.Font("freesansbold.ttf",40)

        mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True,(255,255,255))
        self.pantalla.blit(mi_fuente_final,(220,300))
class Objeto ():
    def __init__(self,x,y,img, x_cambio = 0, y_cambio = 0) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.x_cambio = x_cambio
        self.y_cambio = y_cambio
    
    def cargarImg(self):
    
        imagen = pygame.image.load(self.img)    
        return imagen
    
    def moverX(self):
        self.x+=self.x_cambio

    def moverY(self):
        self.y+=self.y_cambio

    def crearObjeto(self, pantalla):
    # arrojar significa blitt que sirve para posicionar en la pantalla
        pantalla.blit(self.cargarImg(), (self.x,self.y))
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setXcambio(self, x):
        self.x_cambio = x
    def setYcambio(self, y):
        self.y_cambio = y
    
    def hay_colision(self,x,y):
        distancia = math.sqrt((x-self.x)**2 + (y-self.y)**2)
        if distancia <27:
            return True
        else:
            return False

class Bala(Objeto):
    __slots__ = ["bala_visible"]
    def __init__(self, x, y, img,bala_visible = bool, x_cambio=0, y_cambio=0) -> None:
        super().__init__(x, y, img, x_cambio, y_cambio)
        self.bala_visible= bala_visible
 
    
    # funcion disparar bala
    def disparar_bala(self, pantalla):
        self.bala_visible = True
        pantalla.blit(self.cargarImg(),(self.x+16,self.y+10))
    def setYcambio(self):
        self.y -= self.y_cambio
    def setVisible(self,visible = bool):
        self.bala_visible = visible

class Jugador(Objeto):
    def __init__(self, x, y, img = str, x_cambio=0, y_cambio=0, puntaje = 0,vidas = 3) -> None:
        super().__init__(x, y, img, x_cambio, y_cambio)
        self.puntaje = puntaje
        self.vidas = vidas

    def aumentarPuntaje(self):
        self.puntaje+=1
    
    def colision(self):
        self.vidas-=1
    
class Enemigo(Objeto):
    def __init__(self, x, y, img, x_cambio=0, y_cambio=0) -> None:
        super().__init__(x, y, img, x_cambio, y_cambio)
     

        

 


