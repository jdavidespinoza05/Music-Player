#Jose David Espinoza Brenes y Tomás Blando
#Funciones del menu 3ra Progra
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import tkinter as tk


#Funcion de Leer -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def leerarchivo(ruta):
    dicc={}
    with open(ruta, "r") as archivo:
        for x in archivo:
            datos = x.strip().split(";")
            llave= datos[0]
            valores = datos[1:]
            dicc[llave]=valores
    return dicc

#Funciones de Verificar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def verificacionfacturas():
    prop=open("Base de Datos (archivos)/Facturas.txt","r")
    dic={}
    for linea in prop:
        propri = linea.split(";")
        propri[1] = propri[1].replace("\n", "")
        propri[2] = propri[2].replace("\n", "")
        if propri[0] not in dic.keys():
            dic[propri[0]]={"precio":propri[1], "estado":propri[2]}

    prop.close()
    return(dic)

def verificacionadministrador():
    prop=open("Base de Datos (archivos)/Administrador.txt","r")
    dic={}
    for linea in prop:
        propri = linea.split(";")
        propri[1] = propri[1].replace("\n", "")
        if propri[0] not in dic.keys():
            dic[propri[0]]={"nombre":propri[1]}


    prop.close()
    return(dic)

def verificacionpropietario():

    prop=open("Base de Datos (archivos)/Propietario.txt","r")
    dic={}
    for linea in prop:
        propri = linea.split(";")
        propri[3] = propri[3].replace("\n", "")
        if propri[0] not in dic.keys():
            dic[propri[0]]={"nombre":propri[1],"nummembresia":propri[2],"estado":propri[3]}
    lista=list(dic.values())
    lista3=list(dic.keys())
    lista2=[]
    for i in range(0,len(lista)):
        if lista[i]["nummembresia"] not in lista2:
            lista2.append(lista[i]["nummembresia"])
        else:
            del(dic[lista3[i]])

    prop.close()
    return(dic)



def verificacionplaylist():
    prop=open("Base de Datos (archivos)/Playlist.txt","r")
    dic={}
    llaves = verificacionpropietario().keys()
    for linea in prop:
        propri = linea.split(";")
        propri[2] = propri[2].replace("\n", "")
        if propri[0] not in dic.keys():
            if propri[2] in llaves:
                dic[propri[0]]={"nombre":propri[1],"codpropietario":propri[2]}
    prop.close()

    return(dic)


def verificaciongenero():

    prop=open("Base de Datos (archivos)/Genero.txt","r")
    dic={}
    for linea in prop:
        propri = linea.split(";")
        propri[1] = propri[1].replace("\n", "")
        if propri[0] not in dic.keys():
            dic[propri[0]]={"nombre":propri[1]}
    prop.close()
    return(dic)


def verificacionartista():
    prop=open("Base de Datos (archivos)/Artista.txt","r")
    dic={}
    llaves=verificaciongenero().keys()
    for linea in prop:
        propri = linea.split(";")
        if len(propri)>1:
            propri[2] = propri[2].replace("\n", "")
            if propri[0] not in dic.keys():
                if propri[2] in llaves:
                    dic[propri[0]]={"nombre":propri[1],"codgenero":propri[2]}
    prop.close()
    return(dic)


def verificacionalbumes():
    prop=open("Base de Datos (archivos)/Album.txt","r")
    dic={}
    llaves=verificacionartista().keys()
    for linea in prop:
        propri = linea.split(";")
        propri[2] = propri[2].replace("\n", "")
        if propri[0] not in dic.keys():
            if propri[2] in llaves:
                dic[propri[0]]={"nombre":propri[1],"codartista":propri[2]}
    prop.close()
    return(dic)



def verificacioncancion():
    prop=open("Base de Datos (archivos)/Canciones.txt","r")
    dic={}
    llaves1=verificacionartista().keys()
    llaves2=verificacionalbumes().keys()
    llaves3=verificaciongenero().keys()
    llaves4=verificacionplaylist().keys()
    for linea in prop:
        propri = linea.split(";")
        propri[5] = propri[5].replace("\n", "")
        if propri[0] not in dic.keys():
            if propri[2] in llaves1 and propri[3] in llaves2 and propri[4] in llaves3 and propri[5] in llaves4:
                dic[propri[0]]={"nombre":propri[1],"codartista":propri[2],"codalbum":propri[3],"codgenero":propri[4],"codplaylist":propri[5]}
    prop.close()
    return(dic)


#Funciones de Insercion ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def insertarAdmin(dicc, nuevoNombre, nuevoCod):
    nuevoNombre=nuevoNombre.get()    
    nuevoCod=nuevoCod.get()
    
    if nuevoCod in dicc:
        messagebox.showinfo(title="Fallo", message="\nCodigo ya en uso.")
        return dicc

    if nuevoCod.isdigit():
        dicc[nuevoCod]={"nombre":nuevoNombre}
        messagebox.showinfo(title="Completo", message="\nSe insertó correctamente el codigo "+ nuevoCod+ ", el nombre "+ nuevoNombre)

        return dicc

    messagebox.showinfo(title="Fallo", message="Datos invalidos")
    return dicc

def insertarPropietario(dicc, nuevoCod, nuevoNombre, nuevoNum, activo):
    nuevoCod=nuevoCod.get()
    nuevoNombre=nuevoNombre.get()
    nuevoNum=nuevoNum.get()
    activo=activo.get()
    
    if nuevoCod in dicc:
        messagebox.showinfo(title="Fallo", message="\nCodigo ya en uso.")
        return dicc

    if not activo=="1" and not activo=="0":
        messagebox.showinfo(title="Fallo", message="\nError, activo solo puede ser 1 o 0..")
        return dicc

    if nuevoCod.isdigit():
        dicc[nuevoCod]={"nombre":nuevoNombre, "nummembresia":nuevoNum, "estado":activo}
        messagebox.showinfo(title="Completo", message="\nSe insertó correctamente el codigo "+nuevoCod+ ", el nombre "+ nuevoNombre+ ", y el numero de membresia "+ nuevoNum)
        return dicc

    print("\nDatos invalidos.")
    return dicc

def insertarPlaylist(dicc,propietario, nuevoCod, nuevoNombre, nuevoCodP):
    
    nuevoCod=nuevoCod.get()       
    nuevoNombre=nuevoNombre.get()
    nuevoCodP=nuevoCodP.get()
    if nuevoCod in dicc:
        messagebox.showinfo(title="Fallo", message="\nCodigo ya en uso.")
        return dicc

    if nuevoCodP not in propietario:
        messagebox.showinfo(title="Fallo", message="\nEl codigo de propietario no existe, cree un propietario primero.")
        return dicc

    elif nuevoCod.isdigit():
        dicc[nuevoCod]={"nombre":nuevoNombre, "codpropietario":nuevoCodP}
        messagebox.showinfo(title="Completo", message="\nSe insertó correctamente el codigo "+ nuevoCod+ ", el nombre "+ nuevoNombre+ ", y el numero de propietario "+ nuevoCodP)
        return dicc

    messagebox.showinfo(title="Fallo", message="Datos invalidos")
    return dicc


def insertarGenero(dicc, nuevoNombre, nuevoCod, generoMS):
    nuevoNombre=nuevoNombre.get()    
    nuevoCod=nuevoCod.get()
    
    if nuevoCod in dicc:
        messagebox.showinfo(title="Fallo", message="\nCodigo ya en uso.")
        return dicc

    if nuevoCod.isdigit():
        dicc[nuevoCod]={"nombre":nuevoNombre}
        generoMS[nuevoCod]=0
        messagebox.showinfo(title="Completo", message="\nSe insertó correctamente el codigo "+ nuevoCod+ ", el nombre "+ nuevoNombre)
        return dicc, generoMS

    messagebox.showinfo(title="Fallo", message="Datos invalidos")
    return dicc


def insertarArtista(dicc,genero, nuevoCod, nuevoNombre, nuevoCodG, artistaMS):
    
    nuevoCod=nuevoCod.get()
    nuevoNombre=nuevoNombre.get()
    nuevoCodG=nuevoCodG.get()
    
    if nuevoCod in dicc:
        messagebox.showinfo(title="Fallo", message="\nCodigo ya en uso.")
        return dicc
    
    if nuevoCodG not in genero: 
        messagebox.showinfo(title="Fallo", message="\nEl codigo del genero no existe, cree un genero nuevo.")
        return dicc

    if nuevoCod.isdigit():
        dicc[nuevoCod]={"nombre":nuevoNombre, "codgenero":nuevoCodG}
        artistaMS[nuevoCod]=0
        messagebox.showinfo(title="Completo", message="\nSe insertó correctamente el codigo "+ nuevoCod+ " el nombre "+ nuevoNombre+ " y el codigo del genero "+ nuevoCodG)
        return dicc

    messagebox.showinfo(title="Fallo", message="Datos invalidos")
    return dicc


def insertarAlbum(dicc,artista, nuevoCod, nuevoNombre, nuevoCodA, albumMS):
    
    nuevoCod=nuevoCod.get()
    nuevoNombre=nuevoNombre.get()
    nuevoCodA=nuevoCodA.get()
    
    if nuevoCod in dicc:
        messagebox.showinfo(title="Fallo", message="\nCodigo ya en uso.")
        return dicc
    
    if nuevoCodA not in artista:
        messagebox.showinfo(title="Fallo", message="\nEl codigo de artista no existe, cree un artista nuevo.")
        return dicc

    if nuevoCod.isdigit():
        dicc[nuevoCod]={"nombre":nuevoNombre, "codartista":nuevoCodA}
        albumMS[nuevoCod]=0
        messagebox.showinfo(title="Completo", message="\nSe insertó correctamente el codigo "+ nuevoCod+ " el nombre "+ nuevoNombre+ " y el codigo del artista "+ nuevoCodA)
        return dicc

    messagebox.showinfo(title="Fallo", message="Datos invalidos")
    return dicc



def insertarCancion(dicc,artista, album, genero, playlist, nuevoCod, nuevoNombre, nuevoCodA, nuevoCodAl, nuevoCodG, nuevoCodP):
    nuevoCod=nuevoCod.get()
    nuevoNombre=nuevoNombre.get()
    nuevoCodA=nuevoCodA.get()
    nuevoCodAl=nuevoCodAl.get()
    nuevoCodG=nuevoCodG.get()
    nuevoCodP=nuevoCodP.get()
    
    if nuevoCod in dicc:
        messagebox.showinfo(title="Fallo", message="\nCodigo ya en uso.")
        return dicc
    
    if nuevoCodA not in artista:
        messagebox.showinfo(title="Fallo", message="\nEl codigo de artista no existe, cree un artista nuevo.")
        return dicc

    if nuevoCodAl not in album:
        messagebox.showinfo(title="Fallo", message="\nEl codigo de album no existe, cree un album nuevo.")
        return dicc

    if nuevoCodG not in genero:
        messagebox.showinfo(title="Fallo", message="\nEl codigo del genero no existe, cree un genero nuevo.")
        return dicc

    if nuevoCodP not in playlist:
        messagebox.showinfo(title="Fallo", message="\nEl codigo de playlist no existe, cree una playlist nueva.")
        return dicc

    if nuevoCod.isdigit():
        dicc[nuevoCod]=[nuevoNombre, nuevoCodA, nuevoCodAl, nuevoCodG, nuevoCodP]
        dicc[nuevoCod]={"nombre":nuevoNombre, "codartista":nuevoCodA, "codalbum":nuevoCodAl, "codgenero":nuevoCodG, "codplaylist":nuevoCodP}
        messagebox.showinfo(title="Completo", message="\nSe insertó correctamente el codigo "+ nuevoCod+ " el nombre "+ nuevoNombre+ " y los demás codigos.")
        return dicc

    messagebox.showinfo(title="Fallo", message="Datos invalidos")
    return dicc


#Funciones de Buscar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def buscarAdmin(dicc, codadministrador):

    codadministrador=codadministrador.get()
    
    if codadministrador in dicc:
        administrador=dicc[codadministrador]["nombre"]
        messagebox.showinfo(title="Completo", message="\nSe encontro al administrador: "+ administrador)
        return administrador
        
    messagebox.showinfo(title="Fallo", message="\nNo se encontro al administrador.")
    
    return ""

def buscarPropietario(dicc, codpropietario):

    codpropietario=codpropietario.get()
    
    if codpropietario in dicc:
        propietario=dicc[codpropietario]["nombre"]
        messagebox.showinfo(title="Completo", message="\nSe encontro al propietario: "+ propietario)
        return propietario
        
    messagebox.showinfo(title="Fallo", message="\nNo se encontro al propietario.")
    
    return ""


def buscarPlaylist(dicc, codplaylist):

    codplaylist=codplaylist.get()

    if codplaylist in dicc:
        playlist=dicc[codplaylist]["nombre"]

        return playlist,messagebox.showinfo(title="Completo", message="\nSe encontro una playlist: "+ playlist)
        
    messagebox.showinfo(title="Fallo", message="\nNo se encontro la playlist.")

    return ""


def buscarGenero(dicc, codgenero, generoMS):
    codgenero=codgenero.get()

    if codgenero in dicc:
        genero=dicc[codgenero]["nombre"]
        generoMS[codgenero]+=1

        return genero, generoMS, messagebox.showinfo(title="Completo", message="\nSe encontro el genero: "+ genero)
        

    messagebox.showinfo(title="Fallo", message="\nNo se encontro el genero.")
    
    return ""

    
def buscarArtista(dicc, codArtista, artistaMS):

    codArtista=codArtista.get()

    if codArtista in dicc:
        Artista=dicc[codArtista]["nombre"]
        artistaMS[codArtista]+=1

        return Artista, artistaMS, messagebox.showinfo(title="Completo", message="\nSe encontro un artista: "+ Artista)
        
    messagebox.showinfo(title="Fallo", message="\nNo se encontro al artista.")
    
    return ""


def buscarAlbum(dicc, codAlbum, albumMS):

    codAlbum=codAlbum.get()

    if codAlbum in dicc:
            Album=dicc[codAlbum]["nombre"]
            albumMS[codAlbum]+=1

            return Album, albumMS, messagebox.showinfo(title="Completo", message="\nSe encontro un album: "+ Album)
        
    messagebox.showinfo(title="Fallo", message="\nNo se encontro el album.")
    return ""


def buscarCancion(dicc, codCancion):

    codCancion=codCancion.get()

    if codCancion in dicc:
            Cancion=dicc[codCancion]["nombre"]

            return Cancion,messagebox.showinfo(title="Completo", message="\nSe encontro una cancion: "+ Cancion)

        

    messagebox.showinfo(title="Fallo", message="\nNo se encontro la cancion.")

    return ""


#Funciones de Eliminar -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def buscarValor(dicc, valor):
    for llave, subdicc in dicc.items():
        if valor in subdicc.values():
            return llave
    return ""


def eliminarAdmin(diccPr, codpropietario):
    codpropietario=codpropietario.get()
    
    if codpropietario in diccPr:            
        del diccPr[codpropietario]
        messagebox.showinfo(title="Exito", message="\nSe eliminó el administrador")
        return diccPr

    else:
        messagebox.showinfo(title="Fallo", message="\nNo hay administrador que borrar.")
        return diccPr
    
def eliminarPropietario(diccPr,diccPl,diccC,codpropietario):
    codpropietario=codpropietario.get()
    
    if codpropietario in diccPr:
        while True:     
            diccPl, diccC=eliminarPlaylist(diccPl, diccC, buscarValor(diccPl,codpropietario))
            if buscarValor(diccPl, codpropietario) == "":
                break
            
        del diccPr[codpropietario]
        messagebox.showinfo(title="Exito", message="\nSe eliminó el propietario")
        return diccPr,diccPl,diccC

    else:
        messagebox.showinfo(title="Fallo", message="\nNo hay propietario que borrar.")
        return diccPr,diccPl,diccC


def eliminarPlaylist(diccPl, diccC, codplaylist):
    if not isinstance(codplaylist, str):
        codplaylist=codplaylist.get()

    if codplaylist in diccPl:
        while True:
            diccC=eliminarCancion(diccC, buscarValor(diccC, codplaylist))
            if buscarValor(diccC, codplaylist) == "":
                break
        del diccPl[codplaylist]
        messagebox.showinfo(title="Exito", message="\nSe eliminó la playlist.")
        return diccPl, diccC

    else:
        messagebox.showinfo(title="Fallo", message="\nNo hay playlist que borrar.")
        return diccPl, diccC


def eliminarGenero(diccG,diccAr,diccAl,diccC,codgenero):
    if not isinstance(codgenero, str):
        codgenero=codgenero.get()

    if codgenero in diccG:
        while True:
            diccAr, diccAl, diccC=eliminarArtista(diccAr, diccAl, diccC, buscarValor(diccAr, codgenero))
            if buscarValor(diccAr, codgenero) == "":
                break
        del diccG[codgenero]
        messagebox.showinfo(title="Exito", message="\nSe eliminó el genero.")
        return diccG,diccAr,diccAl,diccC

    else:
        messagebox.showinfo(title="Fallo", message="\nNo hay genero que borrar.")
        return diccG,diccAr,diccAl,diccC


def eliminarArtista(diccAr, diccAl, diccC, codartista):
    if not isinstance(codartista, str):
        codartista=codartista.get()

    if codartista in diccAr:
        while True:
            diccAl, diccC=eliminarAlbum(diccAl, diccC, buscarValor(diccAl, codartista))
            if buscarValor(diccAl, codartista) == "":
                break
        del diccAr[codartista]
        messagebox.showinfo(title="Exito", message="\nSe eliminó el artista.")
        return diccAr,diccAl,diccC

    else:
        messagebox.showinfo(title="Fallo", message="\nNo hay artista que borrar.")
        return diccAr,diccAl,diccC



def eliminarAlbum(diccAl, diccC, codalbum):
    if not isinstance(codalbum, str):
        codalbum=codalbum.get()

    if codalbum in diccAl:
        while True:
            diccC=eliminarCancion(diccC, buscarValor(diccC, codalbum))
            if buscarValor(diccC, codalbum) == "":
                break
        del diccAl[codalbum]
        messagebox.showinfo(title="Exito", message="\nSe eliminó el album.")
        return diccAl, diccC

    else:
        messagebox.showinfo(title="Fallo", message="\nNo hay album que borrar.")
        return diccAl, diccC


def eliminarCancion(diccC,codcancion):
    if not isinstance(codcancion, str):
        codcancion=codcancion.get()
    
    if codcancion in diccC:
        del diccC[codcancion]
        messagebox.showinfo(title="Exito", message="\nSe eliminó la cancion.")
        return diccC

    else:
        messagebox.showinfo(title="Fallo", message="\nNo hay cancion que borrar.")
        return diccC


#Funciones de Modificar ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def modificarAdministrador(dicc, cod, nom):
    cod=cod.get()
    nom=nom.get()

    if cod in dicc:

        dicc[cod]["nombre"]=nom
        messagebox.showinfo(title="Exito", message="\nSe cambio el antiguo nombre por: " + dicc[cod]["nombre"])
        

        return dicc

    print("\nNo se encontro el codigo.")
    return dicc

def modificarPropietario(dicc, cod, nom):
    cod=cod.get()
    nom=nom.get()

    if cod in dicc:

        dicc[cod]["nombre"]=nom
        messagebox.showinfo(title="Exito", message="\nSe cambio el antiguo nombre por: " + dicc[cod]["nombre"])
        

        return dicc

    print("\nNo se encontro el codigo.")
    return dicc



def modificarPlaylist(dicc, cod, nom):
    cod=cod.get()
    nom=nom.get()

    if cod in dicc:

        dicc[cod]["nombre"]=nom
        messagebox.showinfo(title="Exito", message="\nSe cambio el antiguo nombre por: " + dicc[cod]["nombre"])

        return dicc

    print("\nNo se encontro el codigo.")
    return dicc


def modificarGenero(dicc, cod, nom):
    cod=cod.get()
    nom=nom.get()
    
    if cod in dicc:

        dicc[cod]["nombre"]=nom
        messagebox.showinfo(title="Exito", message="\nSe cambio el antiguo nombre por: " + dicc[cod]["nombre"])

        return dicc

    print("\nNo se encontro el codigo.")
    return dicc


def modificarArtista(dicc, cod, nom):
    cod=cod.get()
    nom=nom.get()
    
    if cod in dicc:

        dicc[cod]["nombre"]=nom
        messagebox.showinfo(title="Exito", message="\nSe cambio el antiguo nombre por: " + dicc[cod]["nombre"])

        return dicc

    print("\nNo se encontro el codigo.")
    return dicc

def modificarAlbum(dicc, cod, nom):
    cod=cod.get()
    nom=nom.get()
    
    if cod in dicc:

        dicc[cod]["nombre"]=nom
        messagebox.showinfo(title="Exito", message="\nSe cambio el antiguo nombre por: " + dicc[cod]["nombre"])

        return dicc

    print("\nNo se encontro el codigo.")
    return dicc   

def modificarCancion(dicc, cod, nom):
    cod=cod.get()
    nom=nom.get()
    
    if cod in dicc:

        dicc[cod]["nombre"]=nom
        messagebox.showinfo(title="Exito", message="\nSe cambio el antiguo nombre por: " + dicc[cod]["nombre"])

        return dicc

    print("\nNo se encontro el codigo.")
    return dicc


#Funciones de Reporte -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def reportePropietario(dicc, root):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Reporte Propietarios")
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#F5EFE6")

    labelreporte=tk.Label(nueva_ventana, text="Reporte Propietarios", bg="#1A4D2E", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    frame = ttk.Frame(nueva_ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap='none')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for i in dicc:
        text.insert(tk.END, f"\nCodigo de porpietario: {i}\n")
        text.insert(tk.END, "Nombre: "+ dicc[i]["nombre"]+ "\n")
        text.insert(tk.END, "Numero de membresía: "+ dicc[i]["nummembresia"] + "\n")
        text.insert(tk.END, "Estado: "+ dicc[i]["estado"] + "\n\n")

    text.config(state=tk.DISABLED)

def reportePlaylist(dicc, codP, root): #########REVISAR
    bd=0
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Reporte Playlists")
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#F5EFE6")

    labelreporte=tk.Label(nueva_ventana, text="Reporte Playlists", bg="#1A4D2E", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    frame = ttk.Frame(nueva_ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap='none')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    codP=codP.get()

    for i in dicc:
        if dicc[i]["codpropietario"]==codP:
            text.insert(tk.END, f"\nCodigo de la playlist: {i}\n")
            text.insert(tk.END, "Nombre de la playlist: "+ dicc[i]["nombre"]+ "\n")
            text.insert(tk.END, "Codigo del propietario: "+ dicc[i]["codpropietario"] + "\n")
            bd=1

    if bd==0:
        text.insert(tk.END, "\nNo hay ningun propietario con ese codigo que tenga playlist.")

    text.config(state=tk.DISABLED)

def reporteGenero(dicc, root):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Reporte Generos")
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#F5EFE6")

    labelreporte=tk.Label(nueva_ventana, text="Reporte Generos", bg="#1A4D2E", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    frame = ttk.Frame(nueva_ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap='none')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    for i in dicc:
        text.insert(tk.END, f"\nCodigo del genero: {i}\n")
        text.insert(tk.END, "Nombre del genero: "+ dicc[i]["nombre"]+ "\n")

    text.config(state=tk.DISABLED)

def reporteArtista(dicc, cod, root):
    bd=0
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Reporte Artistas")
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#F5EFE6")

    labelreporte=tk.Label(nueva_ventana, text="Reporte Artistas", bg="#1A4D2E", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    frame = ttk.Frame(nueva_ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap='none')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    cod=cod.get()

    for i in dicc:
        if dicc[i]["codgenero"]==cod:
            text.insert(tk.END, f"\nCodigo del artista: {i}\n")
            text.insert(tk.END, "Nombre del artista: "+ dicc[i]["nombre"]+ "\n")
            text.insert(tk.END, "Codigo del genero: "+ dicc[i]["codgenero"] + "\n")
            bd=1

    if bd==0:
        text.insert(tk.END, "\nNo hay ningun artista con ese codigo de genero.")

    text.config(state=tk.DISABLED)

def reporteAlbum(dicc, cod, root):
    bd=0
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Reporte Albumes")
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#F5EFE6")

    labelreporte=tk.Label(nueva_ventana, text="Reporte Albumes", bg="#1A4D2E", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    frame = ttk.Frame(nueva_ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap='none')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    cod=cod.get()

    for i in dicc:
        if dicc[i]["codartista"]==cod:
            text.insert(tk.END, f"\nCodigo del album: {i}\n")
            text.insert(tk.END, "Nombre del album: "+ dicc[i]["nombre"]+ "\n")
            text.insert(tk.END, "Codigo del artista: "+ dicc[i]["codartista"] + "\n")
            bd=1

    if bd==0:
        text.insert(tk.END, "\nNo hay ningun album con ese codigo de artista.")

    text.config(state=tk.DISABLED)

def reporteCancion(dicc, cod, root):
    bd=0
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Reporte Canciones")
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#F5EFE6")

    labelreporte=tk.Label(nueva_ventana, text="Reporte Canciones", bg="#1A4D2E", fg="#EEEEEE", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    frame = ttk.Frame(nueva_ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap='none')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    cod=cod.get()

    for i in dicc:
        if dicc[i]["codartista"]==cod:
            text.insert(tk.END, f"\nCodigo de la cancion: {i}\n")
            text.insert(tk.END, "Nombre de la cancion: "+ dicc[i]["nombre"]+ "\n")
            text.insert(tk.END, "Codigo del artista: "+ dicc[i]["codartista"] + "\n")
            text.insert(tk.END, "Codigo del album: "+ dicc[i]["codalbum"] + "\n")
            text.insert(tk.END, "Codigo del genero: "+ dicc[i]["codgenero"] + "\n")
            text.insert(tk.END, "Codigo de la playlist: "+ dicc[i]["codplaylist"] + "\n")
            bd=1

    if bd==0:
        text.insert(tk.END, "\nNo hay ninguna cancion con ese codigo de artista.")

    text.config(state=tk.DISABLED)

def reporteCancionMR(cancionMR, bdCMR, cancion):
    maxi=max(cancionMR.values())
    if maxi==0:
        messagebox.showinfo(title="Cancion mas reproducida", message="\nNo se ha reproducido ninguna cancion.")
    else:
        for x in cancionMR:
            if cancionMR[x]==maxi:
                bd=1
                messagebox.showinfo(title="Cancion mas reproducida", message="\nLa cancion mas reproducida es: "+cancion[x]["nombre"])


def artistaMC(artista, cancion):
    artistaMC={}
    for x in artista:
        for y in cancion:
            if x==cancion[y]["codartista"]:
                if x in artistaMC:
                    artistaMC[x]+=1
                else:
                    artistaMC[x]=1
                    
    if artistaMC=={}:
        messagebox.showinfo(title="Artista con mas canciones", message="\nNo hay ningun artista con mas canciones.")
        return
    else:
        maxi=max(artistaMC.values())
        for llave, valor in artistaMC.items():
            if valor == maxi:
                messagebox.showinfo(title="Artista con mas canciones", message=f"\nEl artista con mas canciones es: "+artista[llave]["nombre"])

def albumMC(album, cancion):
    albumMC={}
    for x in album:
        for y in cancion:
            if x==cancion[y]["codalbum"]:
                if x in albumMC:
                    albumMC[x]+=1
                else:
                    albumMC[x]=1
                    
    if albumMC=={}:
        messagebox.showinfo(title="Album con mas canciones", message="\nNo hay ningun album con mas canciones.")        
        return
    else:
        maxi=max(albumMC.values())
        for llave, valor in albumMC.items():
            if valor == maxi:
                messagebox.showinfo(title="Album con mas canciones", message=f"\nEl album con mas canciones es: "+album[llave]["nombre"])

def reporteGeneroMS(generoMS, genero):
    maxi=max(generoMS.values())
    if maxi==0:
        messagebox.showinfo(title="Genero mas solicitado", message="\nNo se han solicitado generos aun.")
    else:
        for x in generoMS:
            if generoMS[x]==maxi:
                bd=1
                messagebox.showinfo(title="Genero mas solicitado", message="\nEl genero mas solicitado es: "+ genero[x]["nombre"])


def propietarioMP(propietario, playlist):
    propietarioMP={}
    for x in propietario:
        for y in playlist:
            if x==playlist[y]["codpropietario"]:
                if x in propietarioMP:
                    propietarioMP[x]+=1
                else:
                    propietarioMP[x]=1
                    
    if propietarioMP=={}:
        messagebox.showinfo(title="Propietario con mas playlist", message="\nNo hay ningun propietario con mas playlist.")        
        return
    else:
        maxi=max(propietarioMP.values())
        for llave, valor in propietarioMP.items():
            if valor == maxi:
                messagebox.showinfo(title="Propietario con mas playlist", message=f"\nEl propietario con mas playlist es: "+propietario[llave]["nombre"])

def reporteAlbumMS(albumMS, album):
    maxi=max(albumMS.values())
    if maxi==0:
        messagebox.showinfo(title="Album mas solicitado", message="\nNo se han solicitado albumes aun.")
    else:
        for x in albumMS:
            if albumMS[x]==maxi:
                bd=1
                messagebox.showinfo(title="Album mas solicitado", message="\nEl album mas solicitado es: "+ album[x]["nombre"])

def playlistMC(playlist, cancion):
    playlistMC={}
    for x in playlist:
        for y in cancion:
            if x==cancion[y]["codplaylist"]:
                if x in playlistMC:
                    playlistMC[x]+=1
                else:
                    playlistMC[x]=1
                    
    if playlistMC=={}:
        messagebox.showinfo(title="Playlist con mas canciones", message="\nNo hay ninguna playlist con mas canciones.")        
        return
    else:
        maxi=max(playlistMC.values())
        for llave, valor in playlistMC.items():
            if valor == maxi:
                messagebox.showinfo(title="Playlist con mas canciones", message=f"\nLa playlist con mas canciones es: "+playlist[llave]["nombre"])


def generoMA(genero, artista):
    generoMA={}
    for x in genero:
        for y in artista:
            if x==artista[y]["codgenero"]:
                if x in generoMA:
                    generoMA[x]+=1
                else:
                    generoMA[x]=1
                    
    if generoMA=={}:
        messagebox.showinfo(title="Genero con mas artistas.", message="\nNo hay ningun genero con mas artistas.")
        return
    
    else:
        maxi=max(generoMA.values())
        for llave, valor in generoMA.items():
            if valor == maxi:
                messagebox.showinfo(title="Genero con mas artistas.", message=f"\nEl genero con mas artistas es: "+ genero[llave]["nombre"])


def generoMAlb(genero, artista, album):
    generoMAlb={}
    for x in genero:
        for y in artista:
            if x==artista[y]["codgenero"]:
                for z in album:
                    if y==album[z]["codartista"]:
                        if x in generoMAlb:
                            generoMAlb[x]+=1
                        else:
                            generoMAlb[x]=1
                    
    if generoMA=={}:
        messagebox.showinfo(title="Genero con mas albumes.", message="\nNo hay ningun genero con mas albumes.")
        return
    else:
        maxi=max(generoMAlb.values())
        for llave, valor in generoMAlb.items():
            if valor == maxi:
                messagebox.showinfo(title="Genero con mas albumes.", message=f"\nEl genero con mas albumes es: "+ genero[llave]["nombre"])




def artistaMAlb(artista, album):
    artistaMAlb={}
    for x in artista:
        for y in album:
            if x==album[y]["codartista"]:
                if x in artistaMAlb:
                    artistaMAlb[x]+=1
                else:
                    artistaMAlb[x]=1
                    
    if artistaMAlb=={}:
        messagebox.showinfo(title="Artista con mas albumes.", message="\nNo hay ningun artista con mas albumes.")
        return
    else:
        maxi=max(artistaMAlb.values())
        for llave, valor in artistaMAlb.items():
            if valor == maxi:
                messagebox.showinfo(title="Artista con mas albumes.", message=f"\nEl artista con mas albumes es: "+ artista[llave]["nombre"])

def cancionRP(cancion, playlist):
    cancionRP={}
    for x in playlist:
        for y in cancion:
            if x==cancion[y]["codplaylist"]:
                if y in cancionRP:
                    cancionRP[y]+=1
                else:
                    cancionRP[y]=1
                    
    if cancionRP=={}:
        messagebox.showinfo(title="Cancion mas repetida en playlist.", message="\nNo hay ninguna cancion que mas se repita en una playlist.")
        return
    
    else:
        maxi=max(cancionRP.values())
        for llave, valor in cancionRP.items():
            if valor == maxi:
                messagebox.showinfo(title="Cancion mas repetida en playlist.", message=f"\nLa cancion que mas se repite en playlists es: "+ cancion[llave]["nombre"])

def reporteAlbumNB(albumMS, album):
    maxi=max(albumMS.values())
    mini=min(albumMS.values())
    if maxi==0:
        messagebox.showinfo(title="Album nunca solicitado", message="\nNo se ha solicitado ningun album aun.")

    elif mini>0:
        messagebox.showinfo(title="Album nunca solicitado", message="\nYa se han solicitado todos los albumes.")
        
    else:
        for x in albumMS:
            if albumMS[x]==0:
                messagebox.showinfo(title="Album nunca solicitado", message="\nAlbum nunca solicitado: "+ album[x]["nombre"])

def reporteArtistaNB(artistaMS, artista):
    maxi=max(artistaMS.values())
    mini=min(artistaMS.values())
    if maxi==0:
        messagebox.showinfo(title="Artista nunca solicitado", message="\nNo se ha solicitado ningun artista aun.")

    elif mini>0:
        messagebox.showinfo(title="Artista nunca solicitado", message="\nYa se han solicitado todos los artistas.")

    else:
        for x in artistaMS:
            if artistaMS[x]==0:
                messagebox.showinfo(title="Artista nunca solicitado", message="\nArtista nunca solicitado: "+ artista[x]["nombre"])

def propietarioSP(propietario, playlist):
    propietarioMP={}
    bd=0
    for x in propietario:
        propietarioMP[x]=0
    
    for x in propietario:
        for y in playlist:
            if x==playlist[y]["codpropietario"]:
                if x in propietarioMP:
                    propietarioMP[x]+=1
                else:
                    propietarioMP[x]=1
                bd+=1
                    
    if bd==0:
        messagebox.showinfo(title="Propietario sin playlist.", message="\nNo hay ningun propietario sin playlist.")
        return
    else:
        for llave, valor in propietarioMP.items():
            if valor == 0:
                messagebox.showinfo(title="Propietario sin playlist.", message=f"\nEl propietario o los propietarios sin playlist son: "+ propietario[llave]["nombre"])

def cancionNR(cancionMR, cancion):
    maxi=max(cancionMR.values())
    mini=min(cancionMR.values())
    if maxi==0:
        messagebox.showinfo(title="Cancion nunca reproducida", message="\nNo se han reproducido canciones aun.")

    elif mini>0:
        messagebox.showinfo(title="Cancion nunca reproducida", message="\nYa se han reproducido todas las canciones.")

    else:
        for x in cancionMR:
            if cancionMR[x]==0:
                messagebox.showinfo(title="Cancion nunca reproducida", message="\nCancion nunca reproducida: "+ cancion[x]["nombre"])


#INFO Y CONTACTOS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def info(root):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Información sobre la empresa")
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#F8F4E1")
    nueva_ventana.resizable(False, False)

    labelreporte = tk.Label(nueva_ventana, text="Acerca de nosotros", bg="#543310", fg="#F8F4E1", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    frame = ttk.Frame(nueva_ventana)
    frame.pack(fill=tk.BOTH, expand=True)

    text = tk.Text(frame, wrap='word')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=text.yview)
    text.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    texto_largo = (
        "\nNuestra Historia\n\n"
        "En nuestra empresa, creemos que la música es una experiencia atemporal que merece ser disfrutada en un entorno que refleje su riqueza y profundidad. "
        "Inspirados por los días dorados del vinilo y las radios antiguas, hemos creado un reproductor de música que combina la tecnología moderna con una estética vintage que es tanto suave como agradable.\n\n"
        "Nuestra Misión\n\n"
        "Nuestra misión es ofrecer una experiencia de escucha única que transporte a nuestros usuarios a una época en la que la música se disfrutaba con detenimiento y apreciación. "
        "Queremos que cada interacción con nuestro reproductor de música sea un viaje nostálgico, evocando recuerdos y emociones que solo los sonidos clásicos pueden proporcionar.\n\n"
        "Nuestro Producto\n\n"
        "Consideramos nuestro reproductor de música como un producto que integra la simplicidad y elegancia del diseño vintage con la funcionalidad avanzada de la tecnología actual.\n\n"
        "Nuestro Compromiso\n\n"
        "En nuestra empresa estamos comprometidos con la excelencia y la satisfacción del cliente. Nos esforzamos por ofrecer un producto que no solo cumpla con las expectativas, sino que las supere. "
        "Creemos en la importancia de la atención al detalle y en brindar un servicio al cliente de primera clase.\n\n"
        "Únete a Nosotros\n\n"
        "Te invitamos a unirte a nosotros en este viaje musical. Ya sea que seas un entusiasta del vinilo o simplemente alguien que aprecia un buen diseño y una excelente calidad de sonido, "
        "nuestro reproductor de música está hecho para ti. Revive la magia de la música con este reproductor y descubre cómo el pasado puede encontrarse con el presente de una manera armoniosa y hermosa.\n"
    )
    
    text.insert(tk.END, texto_largo)
    text.config(state=tk.DISABLED)


def contacto(root, contactos):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Contacto")
    nueva_ventana.geometry("400x220")
    nueva_ventana.configure(bg="#F8F4E1")
    nueva_ventana.resizable(False, False)

    labelreporte = tk.Label(nueva_ventana, text="FORMULARIO CONTACTO:", bg="#F8F4E1", fg="#543310", pady=10, font=("Courier New", 15))
    labelreporte.pack(fill=tk.X)

    nombre=tk.Label(nueva_ventana, text="Nombre:", bg="#F8F4E1", fg="#74512D", pady=10, font=("Courier New", 15), width=10)
    nombre.place(x=30, y=40)
    nombre_entry=tk.Entry(nueva_ventana, font=("Courier New", 15), width=15)
    nombre_entry.place(x=153, y=50)

    correo=tk.Label(nueva_ventana, text="Correo:", bg="#F8F4E1", fg="#74512D", pady=10, font=("Courier New", 15), width=10)
    correo.place(x=30, y=75)
    correo_entry=tk.Entry(nueva_ventana, font=("Courier New", 15), width=15)
    correo_entry.place(x=153, y=85)

    telefono=tk.Label(nueva_ventana, text="Telefono:", bg="#F8F4E1", fg="#74512D", pady=10, font=("Courier New", 15), width=10)
    telefono.place(x=30, y=110)
    telefono_entry=tk.Entry(nueva_ventana, font=("Courier New", 15), width=15)
    telefono_entry.place(x=153, y=120)
        
    login_boton=tk.Button(nueva_ventana, text="Aceptar", width=30, bg="#543310", fg="#F8F4E1", command=lambda: insertarContacto(contactos, nombre_entry, correo_entry, telefono_entry))
    login_boton.place(x=100, y=170)


def insertarContacto(contactos, nombre_entry, correo_entry, telefono_entry):
    nombre_entry=nombre_entry.get()
    correo_entry=correo_entry.get()
    telefono_entry=telefono_entry.get()

    if nombre_entry=="" or correo_entry=="" or telefono_entry=="":
        messagebox.showinfo(title="Contactos", message="\nError, favor ingrese datos validos.")
        return contactos
        
    for x in contactos:
        if x[0]==nombre_entry or x[1]==correo_entry or x[2]==telefono_entry:
            messagebox.showinfo(title="Contactos", message="\nError, alguno de los valores ya están registrados.")
            return contactos

    contactos+=[[nombre_entry, correo_entry, telefono_entry]]
    messagebox.showinfo(title="Contactos", message=f"\nContacto {nombre_entry} guardado con exito.")
    return contactos
     

#FACTURACION -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def agregar_linea_al_archivo(nombre_archivo, linea):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(linea+'\n')

def eliminar_linea_de_archivo(nombre_archivo, linea_a_eliminar):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
    lineas = [linea for linea in lineas if linea.strip() != linea_a_eliminar]
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(lineas)
        
        
def destruir(ventana, ventana2, op, cod, facturas, dicc):
    ventana.destroy()
    if ventana2!="":
        ventana2.destroy()
    if op=="no":
        messagebox.showinfo(title="Pago", message="No se realizo el pago de la factura.")
        return
    else:
        if dicc[cod]["estado"]=="1":
            messagebox.showinfo(title="Pago", message="Se realizo el pago de la factura con exito.")
            eliminar_linea_de_archivo("Facturas.txt", cod+";"+facturas[cod]["precio"]+";"+facturas[cod]["estado"])
            del facturas[cod]
        elif dicc[cod]["estado"]=="0":
            dicc[cod]["estado"]="1"
            messagebox.showinfo(title="Pago", message="Se realizo el pago de la factura con exito,\nporfavor salga y reingrese al sistema.")
            eliminar_linea_de_archivo("Facturas.txt", cod+";"+facturas[cod]["precio"]+";"+facturas[cod]["estado"])
            del facturas[cod]
        
        return facturas


def procesarFactura(dicc, cod, ventana2, ventana, facturas, estado):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Factura")
    nueva_ventana.geometry("300x200")
    nueva_ventana.configure(bg="white")
    nueva_ventana.resizable(False, False)

    if cod not in facturas:
        crearFactura(facturas, cod, estado, "prop", nueva_ventana)

    if estado=="inactivo":
        facturas[cod]={"precio":"10","estado":estado}
        precio=int(facturas[cod]["precio"])*0.99
            
    elif estado=="registrado":
        facturas[cod]={"precio":"30","estado":estado}
        precio=int(facturas[cod]["precio"])*0.95
            
    else:
        facturas[cod]={"precio":"40","estado":estado}
        precio=int(facturas[cod]["precio"])

    labelreporte = tk.Label(nueva_ventana, text=f"El monto total es de {precio}", bg="white", fg="black", pady=8, font=("Courier New", 12))
    labelreporte.place(x=20, y=40)

    pregunta=tk.Label(nueva_ventana, text="Desea activar el cobro?", bg="white", fg="black", pady=10, font=("Courier New", 10))
    pregunta.place(x=50, y=90)

    if ventana2=="":
        boton1=tk.Button(nueva_ventana, text="Si", width=10, bg="white", fg="black", command=lambda: destruir(ventana, nueva_ventana, "si", cod, facturas, dicc))
        boton1.place(x=40, y=140)

        boton2=tk.Button(nueva_ventana, text="No", width=10, bg="white", fg="black", command=lambda: destruir(ventana, nueva_ventana, "no", cod, facturas, dicc))
        boton2.place(x=180, y=140)
    else:
        boton1=tk.Button(nueva_ventana, text="Si", width=10, bg="white", fg="black", command=lambda: destruir(nueva_ventana, ventana, "si", cod, facturas, dicc))
        boton1.place(x=40, y=140)

        boton2=tk.Button(nueva_ventana, text="No", width=10, bg="white", fg="black", command=lambda: destruir(nueva_ventana, ventana, "no", cod, facturas, dicc))
        boton2.place(x=180, y=140)
        
def crearFactura(facturas, cod, estado, op, nueva_ventana):
    if cod in facturas:
        messagebox.showinfo(title="Factura", message="Error, ya tiene un factura pendiente.")
        return
    else:
        if estado=="inactivo":
            facturas[cod]={"precio":"10","estado":estado}
            agregar_linea_al_archivo("Facturas.txt", cod+";"+facturas[cod]["precio"]+";"+facturas[cod]["estado"])
            
        elif estado=="registrado":
            facturas[cod]={"precio":"30","estado":estado}
            agregar_linea_al_archivo("Facturas.txt", cod+";"+facturas[cod]["precio"]+";"+facturas[cod]["estado"])
            
        elif estado=="nuevo":
            facturas[cod]={"precio":"40","estado":estado}
            agregar_linea_al_archivo("Facturas.txt", cod+";"+facturas[cod]["precio"]+";"+facturas[cod]["estado"])

        if op=="admin":
            messagebox.showinfo(title="Factura", message="Factura creada con exito.")
            nueva_ventana.destroy()
            
        return facturas
    
def facturacion(dicc, cod, ventana2, ventana, facturas):
    if cod in facturas:
        if cod in dicc:
            nueva_ventana = tk.Toplevel(ventana)
            nueva_ventana.title("Facturacion")
            nueva_ventana.geometry("400x220")
            nueva_ventana.configure(bg="#F8F4E1")
            nueva_ventana.resizable(False, False)

            labelreporte = tk.Label(nueva_ventana, text="Tiene una factura pendiente.", bg="#F8F4E1", fg="#543310", pady=10, font=("Courier New", 12))
            labelreporte.pack(fill=tk.X)

            pregunta=tk.Label(nueva_ventana, text="Desea pagar su factura?:", bg="#F8F4E1", fg="#74512D", pady=12, font=("Courier New", 10), width=10)
            pregunta.pack(fill=tk.X)

            if ventana2=="":
                boton1=tk.Button(nueva_ventana, text="Si", width=10, bg="#543310", fg="#F8F4E1", command=lambda: procesarFactura(dicc, cod, "", nueva_ventana, facturas, facturas[cod]["estado"]))
                boton1.place(x=90, y=130)

                boton2=tk.Button(nueva_ventana, text="No", width=10, bg="#543310", fg="#F8F4E1", command=lambda: destruir(nueva_ventana, "", "no", cod, facturas, dicc))
                boton2.place(x=230, y=130)
                
            else:
                boton1=tk.Button(nueva_ventana, text="Si", width=10, bg="#543310", fg="#F8F4E1", command=lambda: procesarFactura(dicc, cod, ventana2, ventana, facturas, facturas[cod]["estado"]))
                boton1.place(x=90, y=130)

                boton2=tk.Button(nueva_ventana, text="No", width=10, bg="#543310", fg="#F8F4E1", command=lambda: destruir(nueva_ventana, ventana, "no", cod, facturas, dicc))
                boton2.place(x=230, y=130)

            
        else:
            messagebox.showinfo(title="Error", message="\nError al realizar el pago.")
    else:
        nueva_ventana = tk.Toplevel(ventana)
        nueva_ventana.title("Facturacion")
        nueva_ventana.geometry("400x220")
        nueva_ventana.configure(bg="#F8F4E1")
        nueva_ventana.resizable(False, False)

        labelreporte = tk.Label(nueva_ventana, text="No hay pagos pendientes ligados a su\n codigo sin embargo, puede pagar por\nadelantado su siguiente suscripcion.", bg="#F8F4E1", fg="#543310", pady=8, font=("Courier New", 12))
        labelreporte.pack(fill=tk.X)

        pregunta=tk.Label(nueva_ventana, text="Desea pagar su siguiente suscripcion?:", bg="#F8F4E1", fg="#74512D", pady=10, font=("Courier New", 10), width=10)
        pregunta.pack(fill=tk.X)

        if ventana2=="":
            boton1=tk.Button(nueva_ventana, text="Si", width=10, bg="#543310", fg="#F8F4E1", command=lambda: procesarFactura(dicc, cod, "", nueva_ventana, facturas, "registrado"))
            boton1.place(x=90, y=150)
            
            boton2=tk.Button(nueva_ventana, text="No", width=10, bg="#543310", fg="#F8F4E1", command=lambda: destruir(nueva_ventana, "", "no", cod, facturas, dicc))
            boton2.place(x=230, y=150)

        else:
            boton1=tk.Button(nueva_ventana, text="Si", width=10, bg="#543310", fg="#F8F4E1", command=lambda: procesarFactura(dicc, cod, ventana2, ventana, facturas, "registrado"))
            boton1.place(x=90, y=150)
            
            boton2=tk.Button(nueva_ventana, text="No", width=10, bg="#543310", fg="#F8F4E1", command=lambda: destruir(nueva_ventana, ventana, "no", cod, facturas, dicc))
            boton2.place(x=230, y=150)
        
    return dicc



def facturacionAdmin(facturas, ventana, dicc):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Facturacion")
    nueva_ventana.geometry("400x220")
    nueva_ventana.configure(bg="#F8F4E1")
    nueva_ventana.resizable(False, False)

    labelreporte = tk.Label(nueva_ventana, text="Ingrese el codigo del propietario\nal que desea hacerle una factura.", bg="#F8F4E1", fg="#543310", pady=8, font=("Courier New", 12))
    labelreporte.pack(fill=tk.X)

    nuevoCod_entry=tk.Entry(nueva_ventana, font=("Courier New", 12), width=15)
    nuevoCod_entry.place(x=120, y=80)

    boton1=tk.Button(nueva_ventana, text="Aceptar", width=10, bg="#543310", fg="#F8F4E1", command=lambda: procesarFacturaAdmin(dicc, nuevoCod_entry.get(), facturas, nueva_ventana))
    boton1.place(x=155, y=150)

def procesarFacturaAdmin(dicc, cod, facturas, nueva_ventana):
    if cod in dicc:
        if cod in facturas:
            crearFactura(facturas, cod, facturas[cod]["estado"], "admin", nueva_ventana)
            return
        else:
            if dicc[cod]["estado"]=="1":
                crearFactura(facturas, cod, "registrado", "admin", nueva_ventana)
                return
            else:
                crearFactura(facturas, cod, "inactivo", "admin", nueva_ventana)
                return

    else:
        messagebox.showinfo(title="Error", message="\nCodigo no existente.")

    
def descuento(ventana):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Descuentos")
    nueva_ventana.geometry("400x300")
    nueva_ventana.configure(bg="#74512D")
    nueva_ventana.resizable(False, False)

    labelreporte = tk.Label(nueva_ventana, text="\n\nDESCUENTOS ACTUALES\n\n\nUsuario activo: 30$ - 5%\n\nUsuario inactivo: 10$ - 1%\n\nUsuario nuevo: 40$ - 0%", bg="#74512D", fg="#F8F4E1", pady=8, font=("Courier New", 12))
    labelreporte.pack(fill=tk.X)





































