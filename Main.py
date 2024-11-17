import pymongo

# Configuración de MongoDB
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PUERTO}/"
MONGO_BASEDATOS = "Premier_League"

# Conexión a MongoDB
try:
    cliente = pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=2000)
    cliente.server_info()  # Verifica conexión
    print("Conexión exitosa a MongoDB")
except pymongo.errors.ServerSelectionTimeoutError as error_tiempo:
    print("Error de conexión: Tiempo excedido")
    exit()
except pymongo.errors.ConnectionFailure as error_conexion:
    print("Error de conexión: Fallo al conectarse")
    exit()


# Seleccionar la base de datos
db = cliente[MONGO_BASEDATOS]

# Función para insertar un equipo
def InsertEquipo(db, equipo):
    coleccion = db["Equipos"]
    resultado = coleccion.insert_one(equipo)
    print(f"Equipo insertado con ID: {resultado.inserted_id}")

# Función para listar equipos
def ListarEquipos(db):
    coleccion = db["Equipos"]
    print("Equipos en la colección:")
    for equipo in coleccion.find():
        print(equipo)

# Función para eliminar un equipo
def EliminarEquipo(db, filtro):
    coleccion = db["Equipos"]
    resultado = coleccion.delete_one(filtro)  # Cambia a delete_many si quieres eliminar múltiples
    print(f"Documentos eliminados: {resultado.deleted_count}")

# Función para actualizar un equipo
def ActualizarEquipo(db, filtro, nuevos_valores):
    coleccion = db["Equipos"]
    resultado = coleccion.update_one(filtro, {"$set": nuevos_valores})  # Cambia a update_many si actualizas múltiples
    print(f"Documentos actualizados: {resultado.modified_count}")

# Programa principal
if __name__ == "__main__":
    # Inserta un equipo como ejemplo
    #nuevo_equipo = {"nombre": "Leones cf", "Ciudad": "medellin"}
    #InsertEquipo(db, nuevo_equipo)

    #Lista los equipos
    #ListarEquipos(db)

    #Actualiza el equipo "Arsenal"
    filtro_actualizar = {"nombre": "Leones cf", "Ciudad": "medellin"}
    nuevos_valores = {"nombre": "Leones", "Ciudad": "monteria"}
    ActualizarEquipo(db, filtro_actualizar, nuevos_valores)

    # Lista los equipos después de la actualización
    ListarEquipos(db)

    # Elimina el equipo "Arsenal"
    #filtro_eliminar = {"nombre": "leones"}
    #EliminarEquipo(db, filtro_eliminar)

    # Lista los equipos después de la eliminación
    #ListarEquipos(db)
