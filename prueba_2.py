import tkinter

def ingreso():
    usuario = entryuser.get()
    contraseña = entrypassword.get()
    print (usuario,contraseña)

def ajustes():
    ventana2 = tkinter.Tk()
    ventana2.title("Ajustes")
    ventana2.geometry("200x200")
    ventana2.mainloop()

ventana = tkinter.Tk()
ventana.title("Prototipo Juego de ROL")
ventana.geometry("500x300")

def registrar():
    userreg = tkinter.Label(text="Usuario")
    userreg.pack(pady=5)

    entryuserreg = tkinter.Entry(ventana)
    entryuserreg.pack()

    passwordreg = tkinter.Label(ventana, text="Contraseña")
    passwordreg.pack(pady=5)

    entrypasswordreg = tkinter.Entry()
    #entrypasswordreg.config(show="*")
    entrypasswordreg.pack()

user = tkinter.Label(text="Usuario")
user.pack(pady=5)

entryuser = tkinter.Entry(ventana)
entryuser.pack()

password = tkinter.Label(text="Contraseña")
password.pack(pady=5)

entrypassword = tkinter.Entry()
entrypassword.config(show="*")
entrypassword.pack()

login = tkinter.Button(ventana, text="Inicio de sesion", command=ingreso)
login.pack(pady=5)

register = tkinter.Button(ventana, text="Registrarse", command=registrar)
register.pack(pady=5)

opciones = tkinter.Button(ventana, text="Opciones", command=ajustes)
opciones.pack(pady=5)

ventana.mainloop()