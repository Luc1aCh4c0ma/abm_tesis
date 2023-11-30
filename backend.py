import mysql.connector

# Conectarse a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='emperardor'
)

cursor = conn.cursor()

def agregar_producto(nombre, descripcion, precio, categoria_id):
    try:
        cursor.execute(
            "INSERT INTO menu (nombre, descripcion, precio, categoria_id) VALUES (%s, %s, %s, %s)",
            (nombre, descripcion, precio, categoria_id)
        )
        conn.commit()
        return "Producto agregado con éxito."
    except mysql.connector.Error as err:
        return f"Error al agregar producto: {err}"

def modificar_producto(menu_id, nombre, descripcion, precio, categoria_id):
    try:
        cursor.execute(
            "UPDATE menu SET nombre = %s, descripcion = %s, precio = %s, categoria_id = %s WHERE menu_id = %s",
            (nombre, descripcion, precio, categoria_id, menu_id)
        )
        conn.commit()
        return "Producto modificado con éxito."
    except mysql.connector.Error as err:
        return f"Error al modificar producto: {err}"

def desactivar_producto(menu_id):
    try:
        cursor.execute("UPDATE menu SET sin_stock = TRUE WHERE menu_id = %s", (menu_id,))
        conn.commit()
        return "Producto desactivado por falta de stock."
    except mysql.connector.Error as err:
        return f"Error al desactivar producto: {err}"
    
def reactivar_producto(menu_id):
    try:
        cursor.execute("UPDATE menu SET sin_stock = FALSE WHERE menu_id = %s", (menu_id,))
        conn.commit()
        return "Producto reactivado y disponible en el menú."
    except mysql.connector.Error as err:
        return f"Error al reactivar producto: {err}"

def obtener_productos_sin_stock():
    productos_sin_stock = []
    cursor.execute("SELECT menu_id, nombre, descripcion, precio, categoria_id FROM menu WHERE sin_stock = TRUE")
    for (menu_id, nombre, descripcion, precio, categoria_id) in cursor:
        productos_sin_stock.append((menu_id, nombre, descripcion, precio, categoria_id))
    return productos_sin_stock

def listar_productos():
    productos_activos = []
    cursor.execute("SELECT menu_id, nombre, descripcion, precio, categoria_id FROM menu WHERE sin_stock = FALSE AND activo = TRUE")
    for (menu_id, nombre, descripcion, precio, categoria_id) in cursor:
        productos_activos.append((menu_id, nombre, descripcion, precio, categoria_id))
    
    return productos_activos
