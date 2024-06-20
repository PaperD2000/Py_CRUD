#Archivo para instrucciones hacia la DB

import conexion as con

def guardar(persona):
    persona = dict(persona)
    try:
        db = con.conectar()
        cursor = db.cursor()
        columnas = tuple(persona.keys())
        valores = tuple(persona.values())
        sql = """
            INSERT INTO Personas{campos} VALUES(?,?,?,?,?,?)
        """.format(campos = columnas)
        cursor.execute(sql, (valores))
        pcreada = cursor.rowcount>0
        db.commit()
        if pcreada:
            cursor.close()
            db.close()
            return {"Respuesta": pcreada, "mensaje": "Persona Registrada"}
        else:
            cursor.close()
            db.close()
            return {"Respuesta": pcreada, "mensaje": "Persona No Registrada"}

    except Exception as ex:
        if "UNIQUE" in str(ex) and "Correo" in str(ex):
            mensaje = "Ya existe una persona con ese Correo"
        if "UNIQUE" in str(ex) and "DNI" in str(ex):
            mensaje = "Ya existe una persona con ese DNI"
        else:
            mensaje = str(ex)
        cursor.close()
        db.close()
        return {"Respuesta": False, "mensaje": mensaje}
def buscarTodo():
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Personas")
        persons = cursor.fetchall()
        if persons:
            cursor.close()
            db.close()
            return {"Respuesta": True, "personas": persons}
        else:
            cursor.close()
            db.close()
            return {"Respuesta": False, "personas": persons, "mensaje": "No hay personas registradas"}
    except Exception as ex:
        return {"Respuesta": False, "mensaje": str(ex)}

def buscar(dniPersona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Personas WHERE DNI = '{dni}'".format(dni=dniPersona))
        person = cursor.fetchall()
        if person:
            info_p = person[0]
            persona = {"ID": info_p[0], "Nombre": info_p[1], "Apellido": info_p[2], "DNI": info_p[3], "Edad": info_p[4], "Direccion": info_p[5], "Correo": info_p[6]}
            cursor.close()
            db.close()
            return {"Respuesta": True, "personas": persona}
        else:
            cursor.close()
            db.close()
            return {"Respuesta": False, "mensaje": "No existe un registro de la persona"}
    except Exception as ex:
        return {"Respuesta": False, "mensaje": str(ex)}

def actualizar(persona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        persona = dict(persona)
        dnipersona = persona.get("DNI")
        persona.pop('DNI')
        valores = tuple(persona.values())
        sql = """
        UPDATE Personas
        SET Nombre=?,Apellido=?,Edad=?,Direccion=?,Correo=?
        WHERE DNI='{dni}'
        """.format(dni=dnipersona)
        cursor.execute(sql,(valores))
        modificada = cursor.rowcount>0
        db.commit()
        cursor.close()
        db.close()

        if modificada:
            return {"Respuesta": modificada, "mensaje": "Persona actualizada"}
        else:
            return {"Respuesta": modificada, "mensaje": "No hay una persona con ese DNI"}

    except Exception as ex:
        cursor.close()
        db.close()
        return {"Respuesta": False, "mensaje": str(ex)}

def borrar(idPersona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        sql = """
        DELETE FROM Personas 
        WHERE ID ='{id}'
        """.format(id=idPersona)
        cursor.execute(sql)
        eliminada = cursor.rowcount>0
        db.commit()
        cursor.close()
        db.close()

        if eliminada:
            return {"Respuesta": eliminada, "mensaje": "Persona eliminada"}
        else:
            return {"Respuesta": eliminada, "mensaje": "No hay una persona con ese ID"}

    except Exception as ex:
        cursor.close()
        db.close()
        return {"Respuesta": False, "mensaje": str(ex)}