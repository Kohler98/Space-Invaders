import pygame   
from pygame import mixer
import random
import time

from clase import *
# inicializar pygame
pygame.init()

# esto sirve para crear una pantalla
pantalla = Pantalla(800,600)


se_ejecuta = True

# titulo e Icono

pygame.display.set_caption("Invasion Espacial")

#cargar imagen con pygame
icono = pygame.image.load("10. Dia 10\\img\\3.1 ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("10. Dia 10\\img\\10.1 Fondo.jpg")

#  cargar jugador
jugador = Jugador(368,500,"10. Dia 10\\img\\4.1 cohete.png",0,0)


#arreglo de enemigo
nave_enemigo =  []
#cantidad de enemigos
cantidad_enemigo = 8
for i in range(cantidad_enemigo):
    #cargar enemigos en el arreglo
    enemigo = Enemigo(random.randint(0,736),random.randint(50,200),"10. Dia 10\\img\\8.1 enemigo.png",1,50)
    nave_enemigo.append(enemigo)

#  cargar bala
bala = Bala(0,500,"10. Dia 10\\img\\11.1 bala.png",False,0,3)

# cargar musica
mixer.music.load("10. Dia 10\\sounds\\16.3 MusicaFondo.mp3")
mixer.music.play(-1)


# loop del juego
while se_ejecuta:
    #cargar fondo rbg
    # pantalla.fill((205,144,228))
    #cargar fondo
    pantalla.pantalla.blit(fondo,(0,0))
 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or jugador.vidas == 0:
      
            for i in range(len(nave_enemigo)):
                nave_enemigo[i].setY(10000)
    
            pantalla.game_over()
            se_ejecuta = False
          
          
        # presionar teclas evento
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT :
                   
                jugador.setXcambio(-1)
            if evento.key == pygame.K_DOWN :
                jugador.setXcambio(0)
            if evento.key == pygame.K_RIGHT:

                jugador.setXcambio(1)
            if evento.key == pygame.K_UP:

                jugador.setYcambio(-1)
            if evento.key == pygame.K_DOWN:

                jugador.setYcambio(1)
            if evento.key == pygame.K_SPACE:
                
                if not bala.bala_visible:
                    pantalla.sonido('10. Dia 10\\sounds\\16.1 disparo.mp3')
                    bala.setX(jugador.x)
                    bala.setY(jugador.y)
                    bala.disparar_bala(pantalla.pantalla)
 
        #disparar
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar ubicacion del enemigo 
    if len(nave_enemigo)>0:
        if jugador.x>0 and jugador.x <736:

            jugador.moverX()
            jugador.moverY()

        if jugador.x>= 736:
    
            jugador.setX(1)
    
        if jugador.x<= 0:
            jugador.setX(735)
        if jugador.y >=600:
            jugador.setY(0)
        if jugador.y < 0:
            jugador.setY(600)
        for i in nave_enemigo:
            i.moverX()

            if i.x <=0:
                i.setXcambio(random.uniform(0,1))
                i.moverY()
        
            if i.x >=736:
         
                i.setXcambio(random.uniform(-1,0))
                i.moverY()

            # colision
            colision = i.hay_colision(jugador.x,jugador.y)
            if colision:
                jugador.colision()
                i.setX(random.randint(0,736))
                i.setY(random.randint(50,200))
        
            colision = i.hay_colision(bala.x,bala.y)
        
            if colision:
                pantalla.sonido('10. Dia 10\\sounds\\16.2 Golpe.mp3')
            
                bala.setY(500)
                bala.setVisible(False)
    
                jugador.aumentarPuntaje()
                i.setX(random.randint(0,736))
                i.setY(random.randint(50,200))
            
            
            i.crearObjeto(pantalla.pantalla)
    
        # movimiento bala
        if bala.y <=-64:
            bala.setY(500)
            
            bala.setVisible(False)
        if bala.bala_visible:
            bala.disparar_bala(pantalla.pantalla)
            bala.setYcambio()

        jugador.crearObjeto(pantalla.pantalla)
        
        #mostrar puntajes
        pantalla.mostrar_puntaje(10,10,jugador.puntaje)
        pygame.display.update()