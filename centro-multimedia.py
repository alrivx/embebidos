#!/usr/bin/env python
'''
Autor: Alejandro Rivera Nagano
Licencia: MIT (Ver License)
Fecha: 5 de febrero de 2021
'''

import vlc
import time
import os
import re
import random

# Reproduccion de canciones
def playMusic():
    for cancion in musica:
        instance = vlc.Instance()
        media = instance.media_new(cancion)
        player = instance.media_player_new()
        player.set_media(media)
        #Start the parser
        media.parse_with_options(1,0)
        while True:
            if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
                break 
        print('REPRODUCIENDO : '+cancion)
        player.play()
        time.sleep(media.get_duration()/1000)
        player.stop()

# Reproduccion de videos
def playVid():
    for vid_path in videos:
        instance = vlc.Instance()
        media = instance.media_new(vid_path)
        player = instance.media_player_new()
        player.set_media(media)
        player.set_fullscreen(True)
        #Start the parser
        media.parse_with_options(1,0)
        while True:
            if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
                break 
        print('REPRODUCIENDO : '+vid_path)
        player.play()
        time.sleep(media.get_duration()/1000)
        player.stop()



# Listas de archivos a reproducir
fotos=[]
musica=[]
videos=[]

# Extensiones reconocidas
extFotos = ['jpg']
extMusica = ['mp3', 'wav', 'ogg']
extVideos = ['mp4','mkv','avi']


# Busqueda de archivos reproducibles mediante expresiones regulares
for r,d,f in os.walk("/media/pi/"):
    for files in f:
        for patternM in extMusica:
            if re.search(patternM,files):
                musica.append(os.path.join(r,files).replace("._",""))
        for patternV in extVideos:
            if re.search(patternV, files):
                videos.append(os.path.join(r,files).replace("._",""))
        for patternF in extFotos:
            if re.search(patternF, files):
                fotos.append(os.path.join(r,files))


# Eliminar duplicados
aux=[]
for i in musica:
    if (i not in aux):
        aux.append(i)
musica = aux

aux=[]
for i in videos:
    if (i not in aux):
        aux.append(i)
videos = aux

aux=[]
for i in fotos:
    if (i not in aux):
        aux.append(i)
fotos = aux




# Crear listas aleatorias
if (len(musica) > 0):
    random.shuffle(musica)

if (len(videos) > 0):
    random.shuffle(videos)

if (len(fotos) > 0):
    random.shuffle(fotos)

# Funcionamiento
if (len(videos)>0 and len(fotos)<=0 and len(musica)<=0):
    playVid()

elif (len(musica)>0 and len(fotos)<=0 and len(videos)<=0):
    playMusic()

else:
    string = """
    Escoja los medios que quiera reproducir:
    1. Musica
    2. Videos
    """
    print(string)
    ingresado = raw_input()

    if(ingresado == "1"):
        playMusic()
    elif(ingresado == "2"):
        playVid()
    else:
        print('Opcion invalida. Ejecute el programa nuevamente')
