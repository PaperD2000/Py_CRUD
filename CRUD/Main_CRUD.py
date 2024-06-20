import PersonaData as pd

"""
#Registro de una nueva persona
persona = {
    "Nombre": "Saul",
    "Apellido":"Flores",
    "DNI": "123456",
    "Edad": 23,
    "Direccion": "Av 510",
    "Correo": "s@c.com"}

res = pd.guardar(persona)
print(res)

#Buscar a todos los registros
res = pd.buscarTodo()
print(res.get("personas"))

#Buscar a una persona por si DNI
res = pd.buscar("12345")
print(res)


#Actualizar info

persona = {'DNI':'12345', 'Nombre': 'Juan Carlos', 'Apellido': 'Zuniga', 'Edad': 24, 'Direccion': 'Indios Verdes', 'Correo': 'jz@c.com'}
res = pd.actualizar(persona)
print(res)

res = pd.find("12345")
print(res)"""

#Eliminar un Registro
res = pd.buscarTodo()
print(res)