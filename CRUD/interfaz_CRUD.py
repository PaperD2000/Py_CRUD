from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PersonaData as pData


####VENTANA####
v = Tk()
v.title('CRUD Personas')
v.geometry('1000x800')
v.resizable(0,0)
v.state('zoomed')
v.configure(bg='#fff')

####VARIABLES####
txt_id = StringVar()
txt_dni = StringVar()
txt_nombre = StringVar()
txt_apellido = StringVar()
txt_direccion = StringVar()
txt_correo = StringVar()
txt_edad = StringVar()

####FUNCIONES####
def creditos():
    messagebox.showinfo("Creditos",
                        """ Creado por: Daniel Gomez Leyva
                        ---------------------------------
                        Linkedin: 
                        GitHub: 
                        """)
    
def salir():
    exit = messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if exit == 'yes':
        v.destroy()

def save():
    if txt_edad.get().isnumeric():
        per = {"DNI": txt_dni.get(), "NOMBRE": txt_nombre.get(), "APELLIDO": txt_apellido.get(), "EDAD": int(txt_edad.get()), "CORREO": txt_correo.get(), "DIRECCION": txt_direccion.get()}
        res = pData.guardar(per)
        if res.get("Respuesta"):
            llenadoTabla()
            messagebox.showinfo("Ok", res.get("mensaje"))
            limpiarCampos()
        else:
            messagebox.showerror("Error de registro", res.get("mensaje"))
    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("Upss!!!", "La edad debe ser un valor numerico")

def llenadoTabla():
    tabla.delete(*tabla.get_children())
    res = pData.buscarTodo()
    personas = res.get("personas")
    for fila in personas:
        f = list(fila)
        f.pop(0)
        f = tuple(f)
        tabla.insert("", END, text=id, values=f)

def limpiarCampos():
    txt_dni.set("")
    txt_nombre.set("")
    txt_apellido.set("")
    txt_direccion.set("")
    txt_correo.set("")
    txt_edad.set("")
    e_dni.focus()

def search():
    if txt_dni.get() != "":
        r = pData.buscar(txt_dni.get())
        if r.get("Respuesta"):
            persona = r.get("personas")
            txt_nombre.set(persona.get("Nombre"))
            txt_apellido.set(persona.get("Apellido"))
            txt_edad.set(persona.get("Edad"))
            txt_correo.set(persona.get("Correo"))
            txt_direccion.set(persona.get("Direccion"))
        else:
            e_dni.focus()
            limpiarCampos()
            messagebox.showerror("Upss!!!", "No se ha encontrado a esa persona")
    else:
        e_dni.focus()
        limpiarCampos()
        messagebox.showerror("Upss!!!", "Ingresa un DNI")

def update():
    if txt_edad.get().isnumeric():
        per = {"DNI": txt_dni.get(), "NOMBRE": txt_nombre.get(), "APELLIDO": txt_apellido.get(), "EDAD": int(txt_edad.get()), "CORREO": txt_correo.get(), "DIRECCION": txt_direccion.get()}
        res = pData.actualizar(per)
        if res.get("Respuesta"):
            llenadoTabla()
            messagebox.showinfo("Ok", res.get("mensaje"))
            limpiarCampos()
        else:
            messagebox.showerror("Error de registro", res.get("mensaje"))
    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("Upss!!!", "La edad debe ser un valor numerico")

def delete():
    if txt_dni.get() != "":
        res = pData.buscar(txt_dni.get())
        if res.get("Respuesta"):
            per = res.get("personas")
            respuesta = messagebox.askquestion("Confirmar","Deseas eliminar a {nombre} {apellido}?".format(nombre= per.get("Nombre"),apellido= per.get("Apellido")))
            if respuesta == 'yes':
                res = pData.borrar(per.get("ID"))
                if res.get("Respuesta"):
                    llenadoTabla()
                    limpiarCampos()
                    messagebox.showinfo("Ok", res.get("mensaje"))
                else:
                    messagebox.showerror("Upss!!!", "No se logro eliminar a la persona")
        else:
            messagebox.showerror("Upss!!!", "No existe esa persona")
            limpiarCampos()
    else:
        e_dni.focus()
        messagebox.showerror("Upss!!!", "Debes indicar el DNI")


####GUI####

#Casillas de los campos de info
fuente = ('Verdana', 13)
Label(v, text="DNI:", anchor="w", justify="left", width=10, bg='#fff', font=fuente).grid(row=0, column=0, padx=10, pady=5)
Label(v, text="Nombre:", anchor="w", justify="left", width=10, bg='#fff', font=fuente).grid(row=1, column=0, padx=10, pady=5)
Label(v, text="Apellido:", anchor="w", justify="left", width=10, bg='#fff', font=fuente).grid(row=2, column=0, padx=10, pady=5)
Label(v, text="Edad:", anchor="w", justify="left", width=10, bg='#fff', font=fuente).grid(row=3, column=0, padx=10, pady=5)
Label(v, text="Correo:", anchor="w", justify="left", width=10, bg='#fff', font=fuente).grid(row=4, column=0, padx=10, pady=5)
Label(v, text="Direccion:", anchor="w", justify="left", width=10, bg='#fff', font=fuente).grid(row=5, column=0, padx=10, pady=5)

#Inputs
e_dni = ttk.Entry(v, font=fuente, textvariable=txt_dni)
e_dni.grid(row=0, column=1, padx=10, pady=5)
e_dni.focus()

e_nombre = ttk.Entry(v, font=fuente, textvariable=txt_nombre)
e_nombre.grid(row=1, column=1, padx=10, pady=5)

e_apellido = ttk.Entry(v, font=fuente, textvariable=txt_apellido)
e_apellido.grid(row=2, column=1, padx=10, pady=5)

e_edad = ttk.Entry(v, font=fuente, textvariable=txt_edad)
e_edad.grid(row=3, column=1, padx=10, pady=5)

e_correo = ttk.Entry(v, font=fuente, textvariable=txt_correo)
e_correo.grid(row=4, column=1, padx=10, pady=5)

e_direccion = ttk.Entry(v, font=fuente, textvariable=txt_direccion)
e_direccion.grid(row=5, column=1, padx=10, pady=5)

#Botones
ico_save = PhotoImage(file="save.png")
ico_find = PhotoImage(file="find.png")
ico_update = PhotoImage(file="update.png")
ico_delete = PhotoImage(file="delete.png")

ttk.Button(v, text="Guardar", command=save, image=ico_save, compound=LEFT).place(x=40,y=230)
ttk.Button(v, text="Consultar", command=search, image=ico_find, compound=LEFT).place(x=200,y=230)
ttk.Button(v, text="Actualizar", command=update, image=ico_update, compound=LEFT).place(x=40,y=300)
ttk.Button(v, text="Eliminar", command=delete, image=ico_delete, compound=LEFT).place(x=200,y=300)

#Tabla
Label(v, text="LISTA DE PERSONAS", font=('Verdana',16)).place(x=720, y=2)
tabla = ttk.Treeview(v)
tabla.place(x=450, y= 40)
tabla["columns"] = ("DNI","NOMBRE", "APELLIDO", "EDAD", "CORREO","DIRECCION")
tabla.column("#0", width=0, stretch=NO)
tabla.column("DNI", width=100, anchor=CENTER)
tabla.column("NOMBRE", width=150, anchor=CENTER)
tabla.column("APELLIDO", width=150, anchor=CENTER)
tabla.column("EDAD", width=100, anchor=CENTER)
tabla.column("CORREO", width=160, anchor=CENTER)
tabla.column("DIRECCION", width=160, anchor=CENTER)
tabla.heading("#0",text="")
tabla.heading("DNI",text="DNI")
tabla.heading("NOMBRE",text="NOMBRE")
tabla.heading("APELLIDO",text="APELLIDO")
tabla.heading("EDAD",text="EDAD")
tabla.heading("CORREO",text="CORREO")
tabla.heading("DIRECCION",text="DIRECCION")

####MENU####
menuTop = Menu(v)
m_archivo = Menu(menuTop, tearoff=0)
m_archivo.add_command(label="Creditos", command=creditos)
m_archivo.add_command(label="Salir", command=salir)
menuTop.add_cascade(label="Archivo",menu=m_archivo)

m_limpiar = Menu(menuTop, tearoff=0)
m_limpiar.add_command(label="Limpiar", command=limpiarCampos)
menuTop.add_cascade(label="Limpiar",menu=m_limpiar)

m_crud = Menu(menuTop, tearoff=0)
m_crud.add_command(label="Guardar", command=save)
m_crud.add_command(label="Consultar", command=search)
m_crud.add_command(label="Actualizar",command=update)
m_crud.add_command(label="Eliminar", command=delete)
menuTop.add_cascade(label="CRUD",menu=m_crud)


v.config(menu=menuTop)

llenadoTabla()
v.mainloop() #metodo que permite mostrar los cambios que se realicen a la ventana
