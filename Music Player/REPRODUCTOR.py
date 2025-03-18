#Codigo del menu
#DE Jose David Espinoza Brenes y Tomás Blando Reyes
#Tercera Progra Taller

from Backend.funcionesProgra3 import *
import tkinter as tk
from tkinter import *
import pygame

"""
VALIDACIONES y VARIABLES ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
administrador=verificacionadministrador()
propietario=verificacionpropietario()
playlist=verificacionplaylist()
genero=verificaciongenero()
album=verificacionalbumes()
artista=verificacionartista()
cancion=verificacioncancion()
facturas=verificacionfacturas()
contactos=[]
bandera=0
var=0

cancionMR={}
bdCMR=0
generoMS={}
bdGMS=0
albumMS={}
bdAMS=0
artistaMS={}
bdArMS=0

for x in cancion:
    cancionMR[x]=0

for x in genero:
    generoMS[x]=0

for x in album:
    albumMS[x]=0

for x in artista:
    artistaMS[x]=0

"""
FUNCIONES DE INTERFAZ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
def main(opcion, contraseña):
    iconinsertar = PhotoImage(file="Imagenes/musica.png")
    iconbuscar = PhotoImage(file="Imagenes/albumes.png")
    iconeliminar = PhotoImage(file="Imagenes/usuarios.png")
    iconmodificar = PhotoImage(file="Imagenes/pagos.png")
    
    ventana=Toplevel()
    ventana.geometry("1000x435")
    ventana.configure(bg="#F5EFE6")
    ventana.title("Reproductor de Musica")
    ventana.resizable(False, False)

    etiqueta=tk.Label(ventana, text="R e p r o d u c t o r    d e    M u s i c a", bg="#1A4D2E", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    etiqueta.pack(fill=tk.X)

    barra=Menu(ventana, activeborderwidth=30)

    global cancionMR
    global generoMS
    global albumMS
    global artistaMS
    global contactos
    
    if opcion=="Administrador": ######################  ADMINISTRADORES MENU

        #Manteniminento
        pop1=Menu(barra, tearoff=False)
        subpop1=Menu(pop1, tearoff=False)
        subpop2=Menu(pop1, tearoff=False)
        subpop3=Menu(pop1, tearoff=False)
        subpop4=Menu(pop1, tearoff=False)

        subpop1.add_command(label="Administrador", command=lambda: insertarSC(administrador))
        subpop1.add_command(label="Propietario", command=lambda: insertarSC(propietario))
        subpop1.add_command(label="Playlist", command=lambda: insertarSC(playlist))
        subpop1.add_command(label="Genero", command=lambda: insertarSC(genero))
        subpop1.add_command(label="Artista", command=lambda: insertarSC(artista))
        subpop1.add_command(label="Album", command=lambda: insertarSC(album))
        subpop1.add_command(label="Canción", command=lambda: insertarSC(cancion))

        subpop2.add_command(label="Administrador", command=lambda: buscarSC(administrador))
        subpop2.add_command(label="Propietario", command=lambda: buscarSC(propietario))
        subpop2.add_command(label="Playlist", command=lambda: buscarSC(playlist))
        subpop2.add_command(label="Genero", command=lambda: buscarSC(genero))
        subpop2.add_command(label="Artista", command=lambda: buscarSC(artista))
        subpop2.add_command(label="Album", command=lambda: buscarSC(album))
        subpop2.add_command(label="Canción", command=lambda: buscarSC(cancion))

        subpop3.add_command(label="Administrador", command=lambda: eliminarSC(administrador))
        subpop3.add_command(label="Propietario", command=lambda: eliminarSC(propietario))
        subpop3.add_command(label="Playlist", command=lambda: eliminarSC(playlist))
        subpop3.add_command(label="Genero", command=lambda: eliminarSC(genero))
        subpop3.add_command(label="Artista", command=lambda: eliminarSC(artista))
        subpop3.add_command(label="Album", command=lambda: eliminarSC(album))
        subpop3.add_command(label="Canción", command=lambda: eliminarSC(cancion)) 

        subpop4.add_command(label="Administrador", command=lambda: modificarSC(administrador))
        subpop4.add_command(label="Propietario", command=lambda: modificarSC(propietario))
        subpop4.add_command(label="Playlist", command=lambda: modificarSC(playlist))
        subpop4.add_command(label="Genero", command=lambda: modificarSC(genero))
        subpop4.add_command(label="Artista", command=lambda: modificarSC(artista))
        subpop4.add_command(label="Album", command=lambda: modificarSC(album))
        subpop4.add_command(label="Canción", command=lambda: modificarSC(cancion))

        pop1.add_cascade(label="Insercion", menu=subpop1)
        pop1.add_cascade(label="Modificacion", menu=subpop4)
        pop1.add_cascade(label="Consulta", menu=subpop2)
        pop1.add_cascade(label="Eliminacion", menu=subpop3)
        
        barra.add_cascade(label="Mantenimiento", menu=pop1)    


        #Reportes
        pop2=Menu(barra, tearoff=False)
        subpop2_1=Menu(pop2, tearoff=False)
        
        subpop2_1.add_command(label="Propietarios", command=lambda: reportePropietario(propietario, ventana))
        subpop2_1.add_command(label="Playlist", command=lambda: reportes(playlist, ventana))
        subpop2_1.add_command(label="Generos", command=lambda: reporteGenero(genero, ventana))
        subpop2_1.add_command(label="Artista de un genero", command=lambda: reportes(artista, ventana))
        subpop2_1.add_command(label="Albumes", command=lambda: reportes(album, ventana))
        subpop2_1.add_command(label="Canciones", command=lambda: reportes(cancion, ventana))
        ################Arreglar cancion mas reproducida (PONER cancionMR+=1 en reproducir)
        subpop2_1.add_command(label="Cancion mas reproducida", command=lambda: reporteCancionMR(cancionMR, bdCMR, cancion))
        subpop2_1.add_command(label="Artista con mas canciones", command=lambda: artistaMC(artista, cancion))
        subpop2_1.add_command(label="Album con mas canciones", command=lambda: albumMC(album, cancion))
        subpop2_1.add_command(label="Genero mas solicitado", command=lambda: reporteGeneroMS(generoMS, genero))   
        subpop2_1.add_command(label="Propietario con mas playlist", command=lambda: propietarioMP(propietario, playlist))
        subpop2_1.add_command(label="Album mas solicitado", command=lambda: reporteAlbumMS(albumMS, album))
        subpop2_1.add_command(label="Playlist con mas canciones", command=lambda: playlistMC(playlist, cancion))
        subpop2_1.add_command(label="Genero con mas artistas", command=lambda: generoMA(genero, artista))
        subpop2_1.add_command(label="Genero con mas albumes", command=lambda: generoMAlb(genero, artista, album))    
        subpop2_1.add_command(label="Artista con mas albumes", command=lambda: artistaMAlb(artista, album))
        subpop2_1.add_command(label="Cancion mas repetida en playlist", command=lambda: cancionRP(cancion, playlist))  
        subpop2_1.add_command(label="Album nunca buscado", command=lambda: reporteAlbumNB(albumMS, album))   
        subpop2_1.add_command(label="Artista nunca buscado", command=lambda: reporteArtistaNB(artistaMS, artista))    
        subpop2_1.add_command(label="Propietario sin playlist", command=lambda: propietarioSP(propietario, playlist))    
        ################Arreglar cancion nunca reproducida (PONER cancionMR+=1 en reproducir)
        subpop2_1.add_command(label="Cancion nunca reproducida", command=lambda: cancionNR(cancionMR, cancion))  

        
        pop2.add_cascade(label="Reportes solicitados", menu=subpop2_1)    
        barra.add_cascade(label="Reportes", menu=pop2)

        
        #Facturacion
        pop3=Menu(barra, tearoff=False)
        subpop3_1=Menu(pop3, tearoff=False)

        subpop3_1.add_command(label="Facturacion", command=lambda: facturacionAdmin(facturas, ventana, propietario))
        subpop3_1.add_command(label="Descuentos", command=lambda: descuento(ventana))

        pop3.add_cascade(label="Facturacion", menu=subpop3_1)  
        barra.add_cascade(label="Facturacion", menu=pop3)

        
        #Reproductor
        pop4=Menu(barra, tearoff=False)

        pop4.add_command(label="Reproductor", command=lambda:menuReproductor(ventana, cancionMR))
        
        barra.add_cascade(label="Reproductor", menu=pop4)


        #Acerca de
        pop5=Menu(barra, tearoff=False)

        pop5.add_command(label="Informacion de la empresa", command=lambda: info(ventana))
       
        barra.add_cascade(label="Acerca de", menu=pop5)


        #Contacto
        pop6=Menu(barra, tearoff=False)

        pop6.add_command(label="Contacto", command=lambda: contacto(ventana, contactos))

        barra.add_cascade(label="Contacto", menu=pop6)
   
        
        ventana_boton = tk.Button(ventana, text="Salir", bg="#4F6F52", fg="#EEEEEE", font=("Arial", 18), width=6, command=ventana.destroy)
        ventana_boton.place(x=450,y=325)

        inserrboton = tk.Button(ventana,image=iconinsertar,text="MUSICA", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu1(opcion))
        inserl=Label(ventana,text="MUSICA", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        buscboton = tk.Button(ventana,image=iconbuscar,text="ALBUMES", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2(opcion))
        buscl=Label(ventana,text="ALBUMES", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        elimboton=tk.Button(ventana,image=iconeliminar,text="USUARIOS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu3(opcion))
        eliml=Label(ventana,text="USUARIOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        modifboton=tk.Button(ventana,image=iconmodificar,text="PAGOS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu4(opcion, contraseña, ventana))
        modifl=Label(ventana,text="PAGOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        inserl.place(x=210,y=237)
        buscl.place(x=360,y=237)
        eliml.place(x=510,y=237)
        modifl.place(x=660,y=237)

        inserrboton.place(x=210, y=110)
        buscboton.place(x=360,y=110)
        elimboton.place(x=510,y=110)
        modifboton.place(x=660,y=110)

    elif opcion=="Propietario": ######################  PROPIETARIOS MENU

        #Manteniminento
        pop1=Menu(barra, tearoff=False)
        subpop2=Menu(pop1, tearoff=False)

        subpop2.add_command(label="Propietario", command=lambda: buscarSC(propietario))
        subpop2.add_command(label="Playlist", command=lambda: buscarSC(playlist))
        subpop2.add_command(label="Genero", command=lambda: buscarSC(genero))
        subpop2.add_command(label="Artista", command=lambda: buscarSC(artista))
        subpop2.add_command(label="Album", command=lambda: buscarSC(album))
        subpop2.add_command(label="Canción", command=lambda: buscarSC(cancion))

        pop1.add_cascade(label="Consulta", menu=subpop2)
        
        barra.add_cascade(label="Mantenimiento", menu=pop1)    


        #Reportes
        pop2=Menu(barra, tearoff=False)
        subpop2_1=Menu(pop2, tearoff=False)
        
        subpop2_1.add_command(label="Propietarios", command=lambda: reportePropietario(propietario, ventana))
        subpop2_1.add_command(label="Playlist", command=lambda: reportes(playlist, ventana))
        subpop2_1.add_command(label="Generos", command=lambda: reporteGenero(genero, ventana))
        subpop2_1.add_command(label="Artista de un genero", command=lambda: reportes(artista, ventana))
        subpop2_1.add_command(label="Albumes", command=lambda: reportes(album, ventana))
        subpop2_1.add_command(label="Canciones", command=lambda: reportes(cancion, ventana))
        subpop2_1.add_command(label="Cancion mas reproducida", command=lambda: reporteCancionMR(cancionMR, bdCMR, cancion))
        subpop2_1.add_command(label="Artista con mas canciones", command=lambda: artistaMC(artista, cancion))
        subpop2_1.add_command(label="Album con mas canciones", command=lambda: albumMC(album, cancion))
        subpop2_1.add_command(label="Genero mas solicitado", command=lambda: reporteGeneroMS(generoMS, genero))   
        subpop2_1.add_command(label="Propietario con mas playlist", command=lambda: propietarioMP(propietario, playlist))
        subpop2_1.add_command(label="Album mas solicitado", command=lambda: reporteAlbumMS(albumMS, album))
        subpop2_1.add_command(label="Playlist con mas canciones", command=lambda: playlistMC(playlist, cancion))
        subpop2_1.add_command(label="Genero con mas artistas", command=lambda: generoMA(genero, artista))
        subpop2_1.add_command(label="Genero con mas albumes", command=lambda: generoMAlb(genero, artista, album))    
        subpop2_1.add_command(label="Artista con mas albumes", command=lambda: artistaMAlb(artista, album))
        subpop2_1.add_command(label="Cancion mas repetida en playlist", command=lambda: cancionRP(cancion, playlist))  
        subpop2_1.add_command(label="Album nunca buscado", command=lambda: reporteAlbumNB(albumMS, album))   
        subpop2_1.add_command(label="Artista nunca buscado", command=lambda: reporteArtistaNB(artistaMS, artista))    
        subpop2_1.add_command(label="Propietario sin playlist", command=lambda: propietarioSP(propietario, playlist))    
        subpop2_1.add_command(label="Cancion nunca reproducida", command=lambda: cancionNR(cancionMR, cancion))  

        
        pop2.add_cascade(label="Reportes solicitados", menu=subpop2_1)    
        barra.add_cascade(label="Reportes", menu=pop2)

        
        #Facturacion
        pop3=Menu(barra, tearoff=False)
        subpop3_1=Menu(pop3, tearoff=False)

        subpop3_1.add_command(label="Facturacion", command=lambda: facturacion(propietario, contraseña, "", ventana, facturas))
        subpop3_1.add_command(label="Descuentos", command=lambda: descuento(ventana))

        pop3.add_cascade(label="Facturacion", menu=subpop3_1)  
        barra.add_cascade(label="Facturacion", menu=pop3)

        
        #Reproductor
        pop4=Menu(barra, tearoff=False)

        pop4.add_command(label="Reproductor", command=lambda: menuReproductor(ventana, cancionMR))
        
        barra.add_cascade(label="Reproductor", menu=pop4)


        #Acerca de
        pop5=Menu(barra, tearoff=False)

        pop5.add_command(label="Informacion de la empresa", command=lambda: info(ventana))
       
        barra.add_cascade(label="Acerca de", menu=pop5)


        #Contacto
        pop6=Menu(barra, tearoff=False)

        pop6.add_command(label="Contacto", command=lambda: contacto(ventana, contactos))

        barra.add_cascade(label="Contacto", menu=pop6)





        
        
        ventana_boton = tk.Button(ventana, text="Salir", bg="#4F6F52", fg="#EEEEEE", font=("Arial", 18), width=6, command=ventana.destroy)
        ventana_boton.place(x=450,y=325)

        inserrboton = tk.Button(ventana,image=iconinsertar,text="MUSICA", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu1(opcion))
        inserl=Label(ventana,text="MUSICA", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        buscboton = tk.Button(ventana,image=iconbuscar,text="ALBUMES", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2(opcion))
        buscl=Label(ventana,text="ALBUMES", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        elimboton=tk.Button(ventana,image=iconeliminar,text="USUARIOS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu3(opcion))
        eliml=Label(ventana,text="USUARIOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        modifboton=tk.Button(ventana,image=iconmodificar,text="PAGOS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu4(opcion, contraseña, ventana))
        modifl=Label(ventana,text="PAGOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        inserl.place(x=210,y=237)
        buscl.place(x=360,y=237)
        eliml.place(x=510,y=237)
        modifl.place(x=660,y=237)

        inserrboton.place(x=210, y=110)
        buscboton.place(x=360,y=110)
        elimboton.place(x=510,y=110)
        modifboton.place(x=660,y=110)

    elif opcion=="PropietarioSinPagar":

        #Facturacion
        pop3=Menu(barra, tearoff=False)
        subpop3_1=Menu(pop3, tearoff=False)

        subpop3_1.add_command(label="Facturacion", command=lambda: facturacion(propietario, contraseña, "", ventana, facturas))
        subpop3_1.add_command(label="Descuentos", command=lambda: descuento(ventana))

        pop3.add_cascade(label="Facturacion", menu=subpop3_1)  
        barra.add_cascade(label="Facturacion", menu=pop3)

        #Acerca de
        pop5=Menu(barra, tearoff=False)

        pop5.add_command(label="Informacion de la empresa", command=lambda: info(ventana))
       
        barra.add_cascade(label="Acerca de", menu=pop5)

        #Contacto
        pop6=Menu(barra, tearoff=False)

        pop6.add_command(label="Contacto", command=lambda: contacto(ventana, contactos))

        barra.add_cascade(label="Contacto", menu=pop6)

        
        ventana_boton = tk.Button(ventana, text="Salir", bg="#4F6F52", fg="#EEEEEE", font=("Arial", 18), width=6, command=ventana.destroy)
        ventana_boton.place(x=450,y=325)

        modifboton=tk.Button(ventana,image=iconmodificar,text="PAGOS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu4(opcion, contraseña, ventana))
        modifl=Label(ventana,text="PAGOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        modifl.place(x=435,y=237)

        modifboton.place(x=435,y=110)
        
    ventana.config(menu=barra)
    ventana.mainloop()

def submenu1(opcion):
    icon1 = PhotoImage(file="Imagenes/genero.png")
    icon2 = PhotoImage(file="Imagenes/artista.png")
    icon3 = PhotoImage(file="Imagenes/playlist.png")
    
    ventana=Toplevel()
    ventana.geometry("230x600")
    ventana.configure(bg="#1A4D2E")
    ventana.title("Musica")
    ventana.resizable(False, False)
    
    generoboton = tk.Button(ventana,image=icon1,text="MUSICA", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(genero, opcion))
    generolabel = Label(ventana,text="GENEROS", bg="#AF8F6F", fg="#EEEEEE", font=("Arial", 14), width=11)
    
    artistaboton = tk.Button(ventana,image=icon2,text="MUSICA", bg="#74512D", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(artista, opcion))
    artistalabel = Label(ventana,text="ARTISTAS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)
     
    playlistboton = tk.Button(ventana,image=icon3,text="MUSICA", bg="#543310", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(playlist, opcion))
    playlistlabel = Label(ventana,text="PLAYLISTS", bg="#543310", fg="#EEEEEE", font=("Arial", 14), width=11)

    generoboton.place(x=50,y=20)
    artistaboton.place(x=50,y=220)
    playlistboton.place(x=50,y=420)
    
    generolabel.place(x=50, y=147)
    artistalabel.place(x=50, y=347)
    playlistlabel.place(x=50, y=547)


    ventana.mainloop()

def submenu2(opcion):
    icon1 = PhotoImage(file="Imagenes/albumes.png")
    icon2 = PhotoImage(file="Imagenes/cancion.png")
    
    ventana=Toplevel()
    ventana.geometry("230x400")
    ventana.configure(bg="#1A4D2E")
    ventana.title("Albumes")
    ventana.resizable(False, False)
    
    albumboton = tk.Button(ventana,image=icon1,text="ALBUMES", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(album, opcion))
    albumlabel = Label(ventana,text="ALBUMES", bg="#AF8F6F", fg="#EEEEEE", font=("Arial", 14), width=11)
    
    cancionboton = tk.Button(ventana,image=icon2,text="CANCIONES", bg="#74512D", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(cancion, opcion))
    cancionlabel = Label(ventana,text="CANCIONES", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)
    
    albumboton.place(x=50,y=20)
    cancionboton.place(x=50,y=220)

    albumlabel.place(x=50, y=147)
    cancionlabel.place(x=50, y=347)


    ventana.mainloop()

def submenu3(opcion):
    icon1 = PhotoImage(file="Imagenes/admins.png")
    icon2 = PhotoImage(file="Imagenes/propietario.png")
    
    ventana=Toplevel()
    ventana.geometry("230x400")
    ventana.configure(bg="#1A4D2E")
    ventana.title("Usuarios")
    ventana.resizable(False, False)

    if opcion=="Administrador":
        adminboton = tk.Button(ventana,image=icon1,text="ADMINS.", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(administrador, opcion))
        adminlabel = Label(ventana,text="ADMINS.", bg="#AF8F6F", fg="#EEEEEE", font=("Arial", 14), width=11)

        adminlabel.place(x=50, y=147)
        adminboton.place(x=50,y=20)
            
        propboton = tk.Button(ventana,image=icon2,text="PROPS.", bg="#74512D", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(propietario, opcion))
        proplabel = Label(ventana,text="PROPS.", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        propboton.place(x=50,y=220)
        proplabel.place(x=50, y=347)

    else:
        propboton = tk.Button(ventana,image=icon2,text="PROPS.", bg="#74512D", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: submenu2_1(propietario, opcion))
        proplabel = Label(ventana,text="PROPS.", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

        propboton.place(x=50,y=120)
        proplabel.place(x=50, y=247)

    ventana.mainloop()

def submenu4(opcion, cod, ventana2): ####      FACTURACIONNN
    icon1 = PhotoImage(file="Imagenes/facturacion.png")
    icon2 = PhotoImage(file="Imagenes/descuento.png")
    
    ventana=Toplevel()
    ventana.geometry("230x400")
    ventana.configure(bg="#1A4D2E")
    ventana.title("Pagos")
    ventana.resizable(False, False)

    if opcion=="Administrador":
    
        factuboton = tk.Button(ventana,image=icon1,text="FACTURAS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: facturacionAdmin(facturas, ventana, propietario))
        factulabel = Label(ventana,text="FACTURAS", bg="#AF8F6F", fg="#EEEEEE", font=("Arial", 14), width=11)
        
        descuboton = tk.Button(ventana,image=icon2,text="DESCUENTOS", bg="#74512D", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: descuento(ventana))
        desculabel = Label(ventana,text="DESCUENTOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

    elif opcion=="Propietario":
    
        factuboton = tk.Button(ventana,image=icon1,text="FACTURAS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: facturacion(propietario, cod, ventana2, ventana, facturas))
        factulabel = Label(ventana,text="FACTURAS", bg="#AF8F6F", fg="#EEEEEE", font=("Arial", 14), width=11)
        
        descuboton = tk.Button(ventana,image=icon2,text="DESCUENTOS", bg="#74512D", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: descuento(ventana))
        desculabel = Label(ventana,text="DESCUENTOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)

    elif opcion=="PropietarioSinPagar":
    
        factuboton = tk.Button(ventana,image=icon1,text="FACTURAS", bg="#AF8F6F", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: facturacion(propietario, cod, ventana2, ventana, facturas))
        factulabel = Label(ventana,text="FACTURAS", bg="#AF8F6F", fg="#EEEEEE", font=("Arial", 14), width=11)
        
        descuboton = tk.Button(ventana,image=icon2,text="DESCUENTOS", bg="#74512D", fg="#FFFFFF", font=("Arial", 16), width=121, height=120, command=lambda: descuento(ventana))
        desculabel = Label(ventana,text="DESCUENTOS", bg="#74512D", fg="#EEEEEE", font=("Arial", 14), width=11)
    
    factuboton.place(x=50,y=20)
    descuboton.place(x=50,y=220)

    factulabel.place(x=50, y=147)
    desculabel.place(x=50, y=347)


    ventana.mainloop()

def submenu2_1(dicc, opcion):
    ventana=Toplevel()
    ventana.geometry("250x170")
    ventana.configure(bg="#A9B388")
    if dicc==administrador:
        ventana.title("Administrador")
    if dicc==propietario:
        ventana.title("Propietario")
    if dicc==genero:
        ventana.title("Genero")
    if dicc==artista:
        ventana.title("Artista")
    if dicc==album:
        ventana.title("Album")
    if dicc==cancion:
        ventana.title("Cancion")
    if dicc==playlist:
        ventana.title("Playlist")
        
    ventana.resizable(False, False)

    if opcion=="Administrador":
        insertarboton = tk.Button(ventana,text="INSERTAR", bg="#5F6F52", fg="#FEFAE0", font=("Arial", 16), command=lambda: insertarSC(dicc), width=20)
        buscarboton = tk.Button(ventana,text="BUSCAR", bg="#5F6F52", fg="#FEFAE0", font=("Arial", 16), command=lambda: buscarSC(dicc), width=20)
        modifboton = tk.Button(ventana,text="MODIFICAR", bg="#5F6F52", fg="#FEFAE0", font=("Arial", 16), command=lambda: modificarSC(dicc), width=20)
        eliminarboton = tk.Button(ventana,text="ELIMINAR", bg="#5F6F52", fg="#FEFAE0", font=("Arial", 16), command=lambda: eliminarSC(dicc), width=20)

        insertarboton.grid(row=0,column=0)
        buscarboton.grid(row=1,column=0)
        modifboton.grid(row=2,column=0)
        eliminarboton.grid(row=3,column=0)

    else:
        buscarboton = tk.Button(ventana,text="BUSCAR", bg="#5F6F52", fg="#FEFAE0", font=("Arial", 16), command=lambda: buscarSC(dicc), width=20)

        buscarboton.grid(row=1,column=0)

    ventana.mainloop()

def menuReproductor(ventana, cancionMR):
    ventana = tk.Toplevel(ventana)
    ventana.geometry("400x200")
    ventana.configure(bg="#1A4D2E")
    ventana.title("Reproductor")
    ventana.resizable(False, False)
    
    lista = []
    
    etiqueta=tk.Label(ventana, text="REPRODUCTOR", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 12))
    etiqueta.pack(fill=tk.X)

    etiqueta2=tk.Label(ventana, text="Inserte el codigo de la cancion que\ndesea agregar a la cola:", bg="#1A4D2E", fg="#EEEEEE", pady=8, font=("Courier New", 10))
    etiqueta2.pack(fill=tk.X)
    
    nuevoCod_entry = tk.Entry(ventana, font=("Courier New", 15), width=25)
    nuevoCod_entry.place(x=50, y=100)
    
    boton = tk.Button(ventana, text="Agregar a la cola", command=lambda: funcion(lista, nuevoCod_entry.get()), width=15)
    boton.place(x=60, y=140)
    
    boton2 = tk.Button(ventana, text="Reproducir", command=lambda: mp3(lista, ventana, cancionMR), width=15)
    boton2.place(x=230, y=140)
    
    ventana.mainloop()

def funcion(lista, valor):
    if valor in cancion.keys():
        lista.append(valor + ".wav")
        messagebox.showinfo(title="Exito", message="Se agrego la cancion a la lista de reproduccion.")
        print(lista)
    else:
        messagebox.showinfo(title="Fallo", message="Codigo invalido")
        print(lista)
    return lista

def mp3(lista, ventana, cancionMR):
    ventana = tk.Toplevel()
    ventana.geometry("500x100")
    ventana.configure(bg="#393E46")
    ventana.title("Reproductor")
    ventana.resizable(False, False)
    
    if len(lista) < 2:
        ventana.destroy()
        messagebox.showinfo(title="Fallo", message="Largo de la cola insuficiente")
        return
    else:
        pygame.mixer.init()
        var = [0]
        
        anteriorb = tk.Button(ventana, text="ANTERIOR", command=lambda: anterior(lista, var, cancionMR), width=10)
        skipb = tk.Button(ventana, text="SIGUIENTE", command=lambda: skip(lista, var, cancionMR), width=10)
        play = tk.Button(ventana, text="PLAY", command=lambda: funca(lista, var, cancionMR), width=10)
        reiniciar_cola = tk.Button(ventana, text="Reiniciar cola", command=lambda: menuReproductor(ventana, cancionMR), width=10)
        pausa = tk.Button(ventana, text="PAUSAR", command=pygame.mixer.music.pause, width=10)
        despausa = tk.Button(ventana, text="DESPAUSAR", command=pygame.mixer.music.unpause, width=10)
        
        anteriorb.place(x=20, y=10)
        pausa.place(x=110, y=10)
        play.place(x=210, y=10)
        despausa.place(x=310, y=10)
        skipb.place(x=400, y=10)     
        
        reiniciar_cola.place(x=210, y=55)
        
    ventana.mainloop()

def funca(lista, var, cancionMR):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(lista[var[0]])
    pygame.mixer.music.play(1, 0.0, 5000)
    valor = lista[var[0]].replace(".wav", "")
    cancionMR[valor]+=1
    return var, cancionMR

def skip(lista, var, cancionMR):
    if var[0] == len(lista) - 1:
        pygame.mixer.music.stop()
        var[0] = 0
        pygame.mixer.music.load(lista[var[0]])
        pygame.mixer.music.play(1, 0.0, 5000)
    else:
        pygame.mixer.music.stop()
        var[0] += 1
        pygame.mixer.music.load(lista[var[0]])
        pygame.mixer.music.play(1, 0.0, 5000)
    valor = lista[var[0]].replace(".wav", "")
    cancionMR[valor]+=1
    return var, cancionMR

def anterior(lista, var, cancionMR):
    if var[0] == 0:
        pygame.mixer.music.stop()
        var[0] = len(lista) - 1
        pygame.mixer.music.load(lista[var[0]])
        pygame.mixer.music.play(1, 0.0, 5000)
    else:
        pygame.mixer.music.stop()
        var[0] -= 1
        pygame.mixer.music.load(lista[var[0]])
        pygame.mixer.music.play(1, 0.0, 5000)
    valor = lista[var[0]].replace(".wav", "")
    cancionMR[valor]+=1
    return var, cancionMR


def insertarSC(dicc):
    ventanaIN=Toplevel()
    ventanaIN.geometry("500x350")
    ventanaIN.configure(bg="#A9B388")
    ventanaIN.title("Inserción")
    ventanaIN.resizable(False, False)

    global generoMS
    global albumMS
    global artistaMS

    if dicc==administrador: #ADMINISTRADOR
        etiqueta=tk.Label(ventanaIN, text="Insertar Administrador", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNombre=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNombre.place(x=33, y=75)
        nuevoNombre_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNombre_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Insertar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: insertarAdmin(administrador, nuevoNombre_entry, nuevoCod_entry))
        login_boton.place(x=140, y=280)
        
    elif dicc==propietario: #PROPIETARIO
        etiqueta=tk.Label(ventanaIN, text="Insertar Propietario", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNombre=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNombre.place(x=33, y=75)
        nuevoNombre_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNombre_entry.place(x=150, y=85)

        nuevoNum=tk.Label(ventanaIN, text="Membresia:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNum.place(x=21, y=110)
        nuevoNum_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNum_entry.place(x=150, y=120)

        user_type=tk.StringVar()
        user_type.set("1")

        activo=tk.Radiobutton(ventanaIN, text="Activo", variable=user_type, value="1", width=10)
        activo.place(x=200, y=180)
        inactivo=tk.Radiobutton(ventanaIN, text="Inactivo", variable=user_type, value="0", width=10)
        inactivo.place(x=200, y=210)
        
        login_boton=tk.Button(ventanaIN, text="Insertar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: insertarPropietario(propietario, nuevoCod_entry, nuevoNombre_entry, nuevoNum_entry, user_type))
        login_boton.place(x=140, y=280)
        
    elif dicc==playlist: #PLAYLIST
        etiqueta=tk.Label(ventanaIN, text="Insertar Playlist", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNombre=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNombre.place(x=33, y=75)
        nuevoNombre_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNombre_entry.place(x=150, y=85)

        nuevoNum=tk.Label(ventanaIN, text="Propietario:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNum.place(x=2, y=110)
        nuevoNum_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNum_entry.place(x=150, y=120)
        
        login_boton=tk.Button(ventanaIN, text="Insertar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: insertarPlaylist(playlist, propietario, nuevoCod_entry, nuevoNombre_entry, nuevoNum_entry))
        login_boton.place(x=140, y=280)

    elif dicc==genero: #GENERO
        etiqueta=tk.Label(ventanaIN, text="Insertar Genero", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNombre=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNombre.place(x=33, y=75)
        nuevoNombre_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNombre_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Insertar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: insertarGenero(genero, nuevoNombre_entry, nuevoCod_entry, generoMS))
        login_boton.place(x=140, y=280)

    elif dicc==artista: #ARTISTA
        etiqueta=tk.Label(ventanaIN, text="Insertar Artista", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNombre=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNombre.place(x=33, y=75)
        nuevoNombre_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNombre_entry.place(x=150, y=85)

        nuevoNum=tk.Label(ventanaIN, text="Genero:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNum.place(x=33, y=110)
        nuevoNum_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNum_entry.place(x=150, y=120)
        
        login_boton=tk.Button(ventanaIN, text="Insertar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: insertarArtista(artista, genero, nuevoCod_entry, nuevoNombre_entry, nuevoNum_entry, artistaMS))
        login_boton.place(x=140, y=280)

    elif dicc==album: #ALBUM
        etiqueta=tk.Label(ventanaIN, text="Insertar Album", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNombre=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNombre.place(x=33, y=75)
        nuevoNombre_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNombre_entry.place(x=150, y=85)

        nuevoNum=tk.Label(ventanaIN, text="Artista:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNum.place(x=33, y=110)
        nuevoNum_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNum_entry.place(x=150, y=120)
        
        login_boton=tk.Button(ventanaIN, text="Insertar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: insertarAlbum(album, artista, nuevoCod_entry, nuevoNombre_entry, nuevoNum_entry, albumMS))
        login_boton.place(x=140, y=280)

    elif dicc==cancion: #CANCION
        etiqueta=tk.Label(ventanaIN, text="Insertar Cancion", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNombre=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNombre.place(x=33, y=75)
        nuevoNombre_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNombre_entry.place(x=150, y=85)

        codArtista=tk.Label(ventanaIN, text="Artista:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        codArtista.place(x=33, y=110)
        codArtista_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        codArtista_entry.place(x=150, y=120)

        codAlbum=tk.Label(ventanaIN, text="Album:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        codAlbum.place(x=33, y=145)
        codAlbum_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        codAlbum_entry.place(x=150, y=155)

        codGenero=tk.Label(ventanaIN, text="Genero:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        codGenero.place(x=33, y=180)
        codGenero_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        codGenero_entry.place(x=150, y=190)

        codPlaylist=tk.Label(ventanaIN, text="Playlist:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        codPlaylist.place(x=33, y=215)
        codPlaylist_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        codPlaylist_entry.place(x=150, y=225)
        
        login_boton=tk.Button(ventanaIN, text="Insertar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: insertarCancion(cancion, artista, album, genero, playlist, nuevoCod_entry, nuevoNombre_entry, codArtista_entry, codAlbum_entry, codGenero_entry, codPlaylist_entry))
        login_boton.place(x=140, y=280)

    ventanaIN.mainloop()

def buscarSC(dicc):
    
    ventanaIN=Toplevel()
    ventanaIN.geometry("500x250")
    ventanaIN.configure(bg="#A9B388")
    ventanaIN.title("Busqueda")
    ventanaIN.resizable(False, False)

    global generoMS
    global albumMS
    global artistaMS

    if dicc==administrador: #ADMINISTRADOR
        etiqueta=tk.Label(ventanaIN, text="Buscar Administrador", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Buscar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: buscarAdmin(administrador, nuevoCod_entry))
        login_boton.place(x=140, y=150)
        
    elif dicc==propietario: #PROPIETARIO
        etiqueta=tk.Label(ventanaIN, text="Buscar Propietario", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Buscar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: buscarPropietario(propietario, nuevoCod_entry))
        login_boton.place(x=140, y=150)
        
    elif dicc==playlist: #PLAYLIST
        etiqueta=tk.Label(ventanaIN, text="Buscar Playlist", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Buscar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: buscarPlaylist(playlist, nuevoCod_entry))
        login_boton.place(x=140, y=150)

    elif dicc==genero: #GENERO
        
        etiqueta=tk.Label(ventanaIN, text="Buscar Genero", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        login_boton=tk.Button(ventanaIN, text="Buscar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: buscarGenero(genero, nuevoCod_entry, generoMS))
        login_boton.place(x=140, y=150)

    elif dicc==artista: #ARTISTA
        etiqueta=tk.Label(ventanaIN, text="Buscar Artista", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Buscar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: buscarArtista(artista, nuevoCod_entry, artistaMS))
        login_boton.place(x=140, y=150)

    elif dicc==album: #ALBUM
        etiqueta=tk.Label(ventanaIN, text="Buscar Album", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Buscar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: buscarAlbum(album, nuevoCod_entry, albumMS))
        login_boton.place(x=140, y=150)

    elif dicc==cancion: #CANCION
        etiqueta=tk.Label(ventanaIN, text="Buscar Cancion", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Buscar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: buscarCancion(cancion, nuevoCod_entry))
        login_boton.place(x=140, y=150)

    ventanaIN.mainloop()

def eliminarSC(dicc):
    
    ventanaIN=Toplevel()
    ventanaIN.geometry("500x250")
    ventanaIN.configure(bg="#A9B388")
    ventanaIN.title("Eliminacion")
    ventanaIN.resizable(False, False)

    if dicc==administrador: #ADMINISTRADOR
        etiqueta=tk.Label(ventanaIN, text="Eliminar Administrador", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Eliminar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: eliminarAdmin(administrador, nuevoCod_entry))
        login_boton.place(x=140, y=150)
        
    elif dicc==propietario: #PROPIETARIO
        etiqueta=tk.Label(ventanaIN, text="Eliminar Propietario", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Eliminar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: eliminarPropietario(propietario, playlist, cancion, nuevoCod_entry))
        login_boton.place(x=140, y=150)
        
    elif dicc==playlist: #PLAYLIST
        etiqueta=tk.Label(ventanaIN, text="Eliminar Playlist", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Eliminar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: eliminarPlaylist(playlist, cancion, nuevoCod_entry))
        login_boton.place(x=140, y=150)

    elif dicc==genero: #GENERO
        etiqueta=tk.Label(ventanaIN, text="Eliminar Genero", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Eliminar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: eliminarGenero(genero, artista, album, cancion, nuevoCod_entry))
        login_boton.place(x=140, y=150)

    elif dicc==artista: #ARTISTA
        etiqueta=tk.Label(ventanaIN, text="Eliminar Artista", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Eliminar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: eliminarArtista(artista, album, cancion, nuevoCod_entry))
        login_boton.place(x=140, y=150)

    elif dicc==album: #ALBUM
        etiqueta=tk.Label(ventanaIN, text="Eliminar Album", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Eliminar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: eliminarAlbum(album, cancion, nuevoCod_entry))
        login_boton.place(x=140, y=150)

    elif dicc==cancion: #CANCION
        etiqueta=tk.Label(ventanaIN, text="Eliminar Cancion", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)
        
        login_boton=tk.Button(ventanaIN, text="Eliminar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: eliminarCancion(cancion, nuevoCod_entry))
        login_boton.place(x=140, y=150)

    ventanaIN.mainloop()

def modificarSC(dicc):
    
    ventanaIN=Toplevel()
    ventanaIN.geometry("500x250")
    ventanaIN.configure(bg="#A9B388")
    ventanaIN.title("Modificacion")
    ventanaIN.resizable(False, False)

    if dicc==administrador: #ADMINISTRADOR
        etiqueta=tk.Label(ventanaIN, text="Modificar Administrador", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNom=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNom.place(x=33, y=75)
        nuevoNom_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNom_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Modificar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: modificarAdministrador(administrador, nuevoCod_entry, nuevoNom_entry))
        login_boton.place(x=140, y=150)

    elif dicc==propietario: #PROPIETARIO
        etiqueta=tk.Label(ventanaIN, text="Modificar Propietario", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNom=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNom.place(x=33, y=75)
        nuevoNom_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNom_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Modificar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: modificarPropietario(propietario, nuevoCod_entry, nuevoNom_entry))
        login_boton.place(x=140, y=150)
        
    elif dicc==playlist: #PLAYLIST
        etiqueta=tk.Label(ventanaIN, text="Modificar Playlist", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNom=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNom.place(x=33, y=75)
        nuevoNom_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNom_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Modificar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: modificarPlaylist(playlist, nuevoCod_entry, nuevoNom_entry))
        login_boton.place(x=140, y=150)

    elif dicc==genero: #GENERO
        etiqueta=tk.Label(ventanaIN, text="Modificar Genero", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNom=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNom.place(x=33, y=75)
        nuevoNom_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNom_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Modificar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: modificarGenero(genero, nuevoCod_entry, nuevoNom_entry))
        login_boton.place(x=140, y=150)

    elif dicc==artista: #ARTISTA
        etiqueta=tk.Label(ventanaIN, text="Modificar Artista", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNom=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNom.place(x=33, y=75)
        nuevoNom_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNom_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Modificar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: modificarArtista(artista, nuevoCod_entry, nuevoNom_entry))
        login_boton.place(x=140, y=150)

    elif dicc==album: #ALBUM
        etiqueta=tk.Label(ventanaIN, text="Modificar Album", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNom=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNom.place(x=33, y=75)
        nuevoNom_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNom_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Modificar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: modificarAlbum(album, nuevoCod_entry, nuevoNom_entry))
        login_boton.place(x=140, y=150)

    elif dicc==cancion: #CANCION
        etiqueta=tk.Label(ventanaIN, text="Modificar Cancion", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 11))
        etiqueta.pack(fill=tk.X)
        
        nuevoCod=tk.Label(ventanaIN, text="Codigo:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoCod.place(x=33, y=40)
        nuevoCod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoCod_entry.place(x=150, y=50)

        nuevoNom=tk.Label(ventanaIN, text="Nombre:", bg="#A9B388", fg="#393E46", pady=10, font=("Courier New", 15))
        nuevoNom.place(x=33, y=75)
        nuevoNom_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
        nuevoNom_entry.place(x=150, y=85)
        
        login_boton=tk.Button(ventanaIN, text="Modificar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: modificarCancion(cancion, nuevoCod_entry, nuevoNom_entry))
        login_boton.place(x=140, y=150)

    ventanaIN.mainloop()

def reportes(dicc, ventana):
    ventanaIN=Toplevel()
    ventanaIN.geometry("500x200")
    ventanaIN.configure(bg="#A9B388")
    ventanaIN.title("Ingresar Codigo")
    ventanaIN.resizable(False, False)
        
    cod_entry=tk.Entry(ventanaIN, font=("Courier New", 15), width=25)
    cod_entry.place(x=100, y=70)

    if dicc == playlist:
        etiqueta=tk.Label(ventanaIN, text="Ingrese el codigo del propietario del que desea saber las playlist:", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 8))
        etiqueta.pack(fill=tk.X)
        login_boton=tk.Button(ventanaIN, text="Aceptar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: reportePlaylist(dicc, cod_entry, ventana))
        login_boton.place(x=140, y=150)

    if dicc == artista:
        etiqueta=tk.Label(ventanaIN, text="Ingrese el codigo del genero del que desea saber los artistas:", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 8))
        etiqueta.pack(fill=tk.X)
        login_boton=tk.Button(ventanaIN, text="Aceptar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: reporteArtista(dicc, cod_entry, ventana))
        login_boton.place(x=140, y=150)

    if dicc == album:
        etiqueta=tk.Label(ventanaIN, text="Ingrese el codigo del artista del que desea saber sus albumes:", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 8))
        etiqueta.pack(fill=tk.X)
        login_boton=tk.Button(ventanaIN, text="Aceptar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: reporteAlbum(dicc, cod_entry, ventana))
        login_boton.place(x=140, y=150)

    if dicc == cancion:
        etiqueta=tk.Label(ventanaIN, text="Ingrese el codigo del artista del que desea saber sus canciones:", bg="#393E46", fg="#EEEEEE", pady=5, font=("Courier New", 8))
        etiqueta.pack(fill=tk.X)
        login_boton=tk.Button(ventanaIN, text="Aceptar", width=30, bg="#222831", fg="#EEEEEE", command=lambda: reporteCancion(dicc, cod_entry, ventana))
        login_boton.place(x=140, y=150)    

    ventanaIN.mainloop()
    


def registrarPropietario(nuevoCod, nuevoNombre, nuevoNum, etiqueta, ventana, opcion):
    
    nuevoCod=nuevoCod.get()
    nuevoNombre=nuevoNombre.get()
    nuevoNum=nuevoNum.get()

    if nuevoCod in propietario:
        etiqueta.config(text="Codigo ya en uso, intentelo con otro diferente.", justify="center")
        ventana.destroy()
        return propietario

    if nuevoCod.isdigit():
        propietario[nuevoCod]={"nombre":nuevoNombre, "nummembresia":nuevoNum, "estado":"0"}
        etiqueta.config(text= "Se creo el usuario con exito", justify="center")
        crearFactura(facturas, nuevoCod, "nuevo", "prop", "")
        ventana.destroy()
        facturas[nuevoCod]={"precio":"40", "estado":"nuevo"}
        main("PropietarioSinPagar", nuevoCod)
        return propietario

    etiqueta.config(text= "Datos invalidos.", justify="center")
    ventana.destroy()
    return propietario

def cobro(cod, activo, etiqueta, ventana, opcion, contraseña):
    if activo=="1":
        propietario[cod]["estado"]="0"
        etiqueta.config(text= "Factura realizada con exito, bienvenido", justify="center")
        ventana.destroy()
        main("PropietarioSinPagar", contraseña)
        return propietario
    else:
        etiqueta.config(text= "No se realizó el cobro", justify="center")
        ventana.destroy()
        return propietario
    

    
def verificar_login(user_type, user_entry, password_entry, etiqueta):
    opcion=user_type.get()
    usuario=user_entry.get()
    contraseña=password_entry.get()

    global propietario
    global administrador
    global playlist
    global genero
    global artista
    global album
    global cancion
    global facturas

    print(propietario)
    
    if opcion=="Propietario":
        
        if buscarValor(propietario, usuario)=="":
            etiqueta.config(text="No se encontro propietario.", justify="center")
            ventanaNP=tk.Tk()
            ventanaNP.geometry("800x650")
            ventanaNP.configure(bg="#393E46")
            ventanaNP.title("Registrar Propietario")
            ventanaNP.resizable(False, False)

            etiqueta2=tk.Label(ventanaNP, text="Registro", bg="#222831", fg="#EEEEEE", pady=10, font=("Courier New", 15))
            etiqueta2.pack(fill=tk.X)

            user_label=tk.Label(ventanaNP, text="Usuario:", bg="#393E46", fg="#EEEEEE", pady=10, font=("Courier New", 15))
            user_label.place(x=180, y=120)

            user_entry=tk.Entry(ventanaNP, font=("Courier New", 15), width=25)
            user_entry.place(x=320, y=133)

            num_label=tk.Label(ventanaNP, text="Membresia:", bg="#393E46", fg="#EEEEEE", pady=10, font=("Courier New", 15))
            num_label.place(x=167, y=180)

            num_entry=tk.Entry(ventanaNP, font=("Courier New", 15), width=25)
            num_entry.place(x=320, y=193)

            password_label=tk.Label(ventanaNP, text="Contraseña:", bg="#393E46", fg="#EEEEEE", pady=10, font=("Courier New", 15))
            password_label.place(x=167, y=240)

            password_entry=tk.Entry(ventanaNP, font=("Courier New", 15), width=25)
            password_entry.place(x=320, y=253)

            login_boton=tk.Button(ventanaNP, text="Registrarse", width=30, bg="#222831", fg="#EEEEEE", command=lambda: registrarPropietario(password_entry, user_entry, num_entry, etiqueta, ventanaNP, opcion))
            login_boton.place(x=290, y=440)

            ventanaNP.mainloop()

            
        else:
            if not propietario[contraseña]["nombre"]==usuario:
                etiqueta.config(text="Contraseña incorrecta.", justify="center")
            else:
                if propietario[contraseña]["nombre"]==usuario and propietario[contraseña]["estado"]=="1":
                    etiqueta.config(text= "Bienvenido Usuario", justify="center")
                    main(opcion, contraseña)
                elif propietario[contraseña]["nombre"]==usuario and propietario[contraseña]["estado"]=="0":
                    etiqueta.config(text= "Bienvenido Usuario", justify="center")
                    crearFactura(facturas, contraseña, "inactivo", "prop", "")
                    facturas[contraseña]={"precio":"10", "estado":"inactivo"}
                    main("PropietarioSinPagar", contraseña)

            
    elif opcion=="Administrador":
        
        if buscarValor(administrador, usuario)=="":
            etiqueta.config(text="El administrador no existe.", justify="center")
        else:
            if contraseña not in administrador:
                etiqueta.config(text="Contraseña incorrecta.", justify="center")
            else:
                if contraseña==buscarValor(administrador, usuario):
                    etiqueta.config(text="Bienvenido Administrador.", justify="center")
                    main(opcion, contraseña)
                else:
                    etiqueta.config(text="Contraseña incorrecta.", justify="center")
            
    else: 
        etiqueta.config(text="Opcion invalida", justify="center")

def login():
    loginSC=tk.Tk()
    loginSC.geometry("1000x700")
    loginSC.configure(bg="#393E46")
    loginSC.title("Reproductor de Musica")
    loginSC.resizable(False, False)

    etiqueta=tk.Label(loginSC, text="Inicio de Sesion", bg="#222831", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    etiqueta.pack(fill=tk.X)

    user_label=tk.Label(loginSC, text="Usuario:", bg="#393E46", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    user_label.place(x=270, y=150)

    user_entry=tk.Entry(loginSC, font=("Courier New", 15), width=25)
    user_entry.place(x=410, y=163)

    password_label=tk.Label(loginSC, text="Contraseña:", bg="#393E46", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    password_label.place(x=257, y=200)

    password_entry=tk.Entry(loginSC, show="*", font=("Courier New", 15), width=25)
    password_entry.place(x=410, y=213)

    user_type=tk.StringVar()
    user_type.set("Propietario")

    user_boton=tk.Radiobutton(loginSC, text="Propietario", variable=user_type, value="Propietario", width=15)
    user_boton.place(x=435, y=300)

    admin_boton=tk.Radiobutton(loginSC, text="Administrador", variable=user_type, value="Administrador", width=15)
    admin_boton.place(x=435, y=350)

    etiqueta_principal = tk.Label(loginSC, text="", bg="#393E46", fg="#EEEEEE", font=("Arial", 12))
    etiqueta_principal.pack(fill=tk.X, pady=40)

    login_boton=tk.Button(loginSC, text="Iniciar Sesión", width=30, bg="#222831", fg="#EEEEEE", command=lambda: verificar_login(user_type, user_entry, password_entry, etiqueta_principal))
    login_boton.place(x=393, y=500)
    
    loginSC.mainloop()

login()


    

"""    

    print("\n           REPRODUCTOR DE MUSICA")
    print("\n       David Espinoza y Tomás Blando")

    print("\n--------------------------------------------")
    print("\n1. Inserción.")
    print("2. Búsqueda.")
    print("3. Eliminar.")
    print("4. Modificar.")
    print("5. Reproducir.")
    print("6. Reportes.")
    print("7. Salir.")
    print("\n--------------------------------------------")
    
    opcion=input("\n\nIngrese el número de la acción que desea realizar: ")
    
    if opcion=="1":
        print    ("\n              Inserción")

        print("\n\n+ + + + + + + + + + + + + + + + + + + + + + + +")
        print("\n1. Propietario.")
        print("2. Playlist.")
        print("3. Genero.")
        print("4. Artista.")
        print("5. Album.")
        print("6. Canción.")
        print("\n+ + + + + + + + + + + + + + + + + + + + + + + +")

        op=input("\nIngrese el número de lo que desea insertar: ")

        if op=="1":
            propietario=insertarPropietario(propietario)

        elif op=="2":
            playlist=insertarPlaylist(playlist,propietario)

        elif op=="3":
            genero=insertarGenero(genero)

        elif op=="4":
            artista=insertarArtista(artista,genero)

        elif op=="5":
            album=insertarAlbum(album,artista)

        elif op=="6":
            cancion=insertarCancion(cancion,artista,album,genero,playlist)

        
    elif opcion=="2":

        print    ("\n           Búsqueda")
        print("\n\n* * * * * * * * * * * * * * * * * * * * * * *")
        print("\n1. Propietario.")
        print("2. Playlist.")
        print("3. Genero.")
        print("4. Artista.")
        print("5. Album.")
        print("6. Canción.")
        print("\n* * * * * * * * * * * * * * * * * * * * * * *")

        op=input("\nIngrese el número de lo que desea buscar: ")

        if op=="1":
            buscarPropietario(propietario)
        elif op=="2":
            buscarPlaylist(playlist)
        elif op=="3":
            x, generoMS=buscarGenero(genero, generoMS)
            bdGMS+=1
        elif op=="4":
            x, artistaMS=buscarArtista(artista, artistaMS)
            bdArMS+=1
        elif op=="5":
            x, albumMS=buscarAlbum(album, albumMS)
            bdAMS+=1
        elif op=="6":
            buscarCancion(cancion)
        
    elif opcion=="3":

        print    ("\n              Eliminar")        
        print("\n\n. . . . . . . . . . . . . . . . . . . . . . .")
        print("\n1. Propietario.")
        print("2. Playlist.")
        print("3. Genero.")
        print("4. Artista.")
        print("5. Album.")
        print("6. Canción.")
        print("\n. . . . . . . . . . . . . . . . . . . . . . .")

        op3=input("\nIngrese el número de lo que desea eliminar: ")

        if op3=="1":
            propietario,playlist,cancion=eliminarPropietario(propietario,playlist,cancion,input("\nIngrese el codigo del propietario: "))
        elif op3=="2":
            playlist,cancion=eliminarPlaylist(playlist,cancion,input("\nIngrese el codigo de la playlist: "))
        elif op3=="3":
            genero,artista,album,cancion=eliminarGenero(genero,artista,album,cancion,input("\nIngrese el codigo del genero: "))
        elif op3=="4":
            artista,album,cancion=eliminarArtista(artista,album,cancion,input("\nIngrese el codigo del artista: "))
        elif op3=="5":
            album,cancion=eliminarAlbum(album,cancion,input("\nIngrese el codigo del album: "))
        elif op3=="6":
            cancion=eliminarCancion(cancion,input("\nIngrese el codigo de la cancion: "))


    elif opcion=="4":
        
        print    ("\n             Modificar")
        print("\n\n% % % % % % % % % % % % % % % % % % % % % % %")
        print("\n1. Propietario.")
        print("2. Playlist.")
        print("3. Genero.")
        print("4. Artista.")
        print("5. Album.")
        print("6. Canción.")
        print("\n% % % % % % % % % % % % % % % % % % % % % % %")

        op3=input("\nIngrese el número de lo que desea modificar: ")

        if op3=="1":
            propietario=modificarPropietario(propietario)
            
        elif op3=="2":
            playlist=modificarPlaylist(playlist)
            
        elif op3=="3":
            genero=modificarGenero(genero)
            
        elif op3=="4":
            artista=modificarArtista(artista)
            
        elif op3=="5":
            album=modificarAlbum(album)
            
        elif op3=="6":
            cancion=modificarCancion(cancion)

        #print(propietario, "\n")
        #print(playlist, "\n")
        #print(genero, "\n")
        #print(artista, "\n")
        #print(album, "\n")
        #print(cancion, "\n")
            

    elif opcion=="5":
        bd=0
        oC="1"
        print("\n       Reproducir\n")
        cola=[]
        if len(cancion)>0:
            while len(cola)!=5:
                if bd==1:
                    print("\nDesea agregar otra cancion a la cola?\n1 si.\n0 no.")
                    oC=input("\nQue desea hacer?: ")
                if oC=="1":
                    codcancion=input("\nIngrese codigo de cancion: ")
                    if codcancion not in cancion.keys():
                        print("\nCancion no encontrada.")
                    else:
                        cola.append(codcancion+".wav")
                        if codcancion in cancionMR:
                            cancionMR[codcancion]+=1
                        else:    
                            cancionMR[codcancion]=1
                        bd=1
                        bdCMR+=1
                elif oC=="0":
                    break

                else:
                    print("\nDato invalido.")

        else:
            print("\nLa cola de canciones está vacia")

        for i in range(0,len(cola)):
            print("\nReproduciendo...")
            playsound(cola[i])



    elif opcion=="6":

        print    ("\n                 Reportes")
        print("\n- - - - - - - - - - - - - - - - - - - - - - -")
        print("\n1. Propietario.")
        print("2. Playlist.")
        print("3. Genero.")
        print("4. Artista.")
        print("5. Album.")
        print("6. Canción.")
        print("7. Cancion mas reproducida.")
        print("8. Artista con mas canciones.")
        print("9. Album con mas canciones.")
        print("10. Genero mas solicitado.")
        print("11. Propietario con mas playlist.")
        print("12. Album mas solicitado.")
        print("13. Playlist con mas canciones.")
        print("14. Genero con mas artistas.")
        print("15. Genero con mas albumes.")
        print("16. Artista con mas albumes.")
        print("17. Cancion que mas se repite en una playlist.")
        print("18. Album nunca buscado.")
        print("19. Artista nunca buscado.")
        print("20. Propietario sin playlist.")
        print("21. Cancion nunca reproducida")
        print("\n- - - - - - - - - - - - - - - - - - - - - - -")

        op3=input("\nIngrese el número de lo que desea saber el reporte: ")

        if op3=="1":
            reportePropietario(propietario)
       
        elif op3=="2":
            reportePlaylist(playlist)
              
        elif op3=="3":
            reporteGenero(genero)
          
        elif op3=="4":
            reporteArtista(artista)
            
        elif op3=="5":
            reporteAlbum(album)
               
        elif op3=="6":
            reporteCancion(cancion)

        elif op3=="7":
            if bdCMR==0:
                print("\nNo se han reproducido canciones aun.")
            else:
                maxi=max(cancionMR.values())
                for llave, valor in cancionMR.items():
                    if valor == maxi:
                        print("\nLa cancion mas reproducida es:", cancion[llave]["nombre"])
                
        elif op3=="8":
            artistaMC(artista, cancion)

        elif op3=="9":
            albumMC(album, cancion)

        elif op3=="10":
            if bdGMS==0:
                print("\nNo se han solicitado generos aun.")
            else:
                maxi=max(generoMS.values())
                for llave, valor in generoMS.items():
                    if valor == maxi:
                        print("\nEl genero mas solicitado es:", genero[llave]["nombre"])
          
        elif op3=="11":
            propietarioMP(propietario, playlist)

        elif op3=="12":
            if bdAMS==0:
                print("\nNo se han solicitado albumes aun.")
            else:
                maxi=max(albumMS.values())
                for llave, valor in albumMS.items():
                    if valor == maxi:
                        print("\nEl album mas solicitado es:", album[llave]["nombre"])

        elif op3=="13":
            playlistMC(playlist, cancion)

        elif op3=="14":
            generoMA(genero, artista)

        elif op3=="15":
            generoMAlb(genero, artista, album)

        elif op3=="16":
            artistaMAlb(artista, album)

        elif op3=="17":
            cancionRP(cancion, playlist)
            
        elif op3=="18": 
            if bdAMS==0:
                print("\nNo se han buscado albumes aun.")
            else:
                for llave, valor in albumMS.items():
                    if valor == 0:
                        print("\nEl album o los albumes nunca buscados son:", album[llave]["nombre"])

        elif op3=="19":
            if bdArMS==0:
                print("\nNo se han buscado artistas aun.")
            else:
                for llave, valor in artistaMS.items():
                    if valor == 0:
                        print("\nEl artista o los artistas nunca buscados son:", artista[llave]["nombre"])

        elif op3=="20":
            propietarioSP(propietario, playlist)

        elif op3=="21":
            if bdCMR==0:
                print("\nNo se han reproducido canciones aun.")
            else:
                for llave, valor in cancionMR.items():
                    if valor == 0:
                        print("\nLa cancion o las canciones nunca reproducidas son:", cancion[llave]["nombre"])            


    elif opcion=="7":
        print("\nSaliendo del menú...")
        break

"""    

        
