import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
import backend

conn = backend.conn
cursor = backend.cursor
def agregar():
    nombre = nombre_entry.get()
    descripcion = descripcion_entry.get()
    precio = float(precio_entry.get())
    categoria_id = categoria_combo.current() + 1
    resultado.set(backend.agregar_producto(nombre, descripcion, precio, categoria_id))
    listar_productos()

def modificar():
    menu_id = int(menu_id_entry.get())
    nombre = nombre_entry.get()
    descripcion = descripcion_entry.get()
    precio = float(precio_entry.get())
    categoria_id = categoria_combo.current() + 1
    resultado.set(backend.modificar_producto(menu_id, nombre, descripcion, precio, categoria_id))
    listar_productos()

def eliminar():
    menu_id_text = menu_id_entry.get()
    if menu_id_text:
        menu_id = int(menu_id_text)
        resultado.set(backend.desactivar_producto(menu_id))
        listar_productos()
    else:
        resultado.set("Ingresa un ID válido para eliminar.")

def reactivar():
    menu_id_text = menu_id_entry.get()
    if menu_id_text:
        menu_id = int(menu_id_text)
        resultado.set(backend.reaktivar_producto(menu_id))
        listar_productos()
    else:
        resultado.set("Ingresa un ID válido para reactivar.")
def listar_productos():
    productos_activos = backend.listar_productos()

    lista = tk.StringVar()
    productos_listbox = tk.Listbox(frame, listvariable=lista, width=40)
    productos_listbox.grid(row=5, column=0, columnspan=3)

    for producto in productos_activos:
        # Agregar cada producto a la lista, no sobrescribirla
        productos_listbox.insert(tk.END, f"{producto[0]}: {producto[1]}, {producto[2]}, {producto[3]}, {producto[4]}")

    # Agrega un botón para actualizar la lista de productos en el menú principal
    actualizar_menu_button = ttk.Button(frame, text="Actualizar Menú", command=listar_productos)
    actualizar_menu_button.grid(row=8, column=2)
    

def mostrar_sin_stock():
    productos_sin_stock = backend.obtener_productos_sin_stock()

    # Verifica si la ventana ya existe, y si no, crea una nueva
    if not hasattr(root, 'ventana_sin_stock'):
        ventana_sin_stock = tk.Toplevel(root)
        ventana_sin_stock.title("Productos sin Stock")
        root.ventana_sin_stock = ventana_sin_stock  # Asigna la ventana a la raíz
    else:
        ventana_sin_stock = root.ventana_sin_stock

    # Borra los widgets anteriores
    for widget in ventana_sin_stock.winfo_children():
        widget.destroy()

    lista_sin_stock = tk.StringVar()
    productos_listbox = tk.Listbox(ventana_sin_stock, listvariable=lista_sin_stock, width=40)
    productos_listbox.grid(row=0, column=0, columnspan=3)

    for producto in productos_sin_stock:
        producto_str = f"{producto[0]}: {producto[1]}, {producto[2]}, {producto[3]}, {producto[4]}"
        productos_listbox.insert(tk.END, producto_str)

    # Agrega un botón "Actualizar" en la misma ventana
    actualizar_sin_stock_button = ttk.Button(ventana_sin_stock, text="Actualizar", command=mostrar_sin_stock)
    actualizar_sin_stock_button.grid(row=1, column=0)

    # Variable de control para rastrear la selección de un producto
    producto_seleccionado = tk.StringVar()

    def seleccionar_producto(event):
        seleccion = productos_listbox.curselection()
        if seleccion:
            menu_id = productos_sin_stock[seleccion[0]][0]
            producto_seleccionado.set(menu_id)
            reactivar_button.config(state=tk.NORMAL)

    productos_listbox.bind('<<ListboxSelect>>', seleccionar_producto)

    # Botón "Reactivar" inicialmente deshabilitado
    reactivar_button = ttk.Button(ventana_sin_stock, text="Reactivar", state=tk.DISABLED, command=lambda: reactivar_producto(producto_seleccionado.get()))
    reactivar_button.grid(row=2, column=0)

productos_sin_stock = []

def reactivar_producto(menu_id):
    resultado.set(backend.reactivar_producto(menu_id))
    
    # Busca el producto en la lista de productos sin stock
    producto_reactivado = None
    for producto in productos_sin_stock:
        if producto[0] == menu_id:
            producto_reactivado = producto
            break
    
    if producto_reactivado:
        # Agrega el producto nuevamente al menú principal
        menu_id, nombre, descripcion, precio, categoria_id = producto_reactivado
        backend.agregar_producto(nombre, descripcion, precio, categoria_id)
        
        # Elimina el producto de la lista de productos sin stock
        productos_sin_stock.remove(producto_reactivado)

        # Refresca la lista de productos sin stock
        mostrar_sin_stock()


root = tk.Tk()
root.title("Menú de Bar")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Campos de entrada
nombre_label = ttk.Label(frame, text="Nombre:")
nombre_label.grid(row=0, column=0)
nombre_entry = ttk.Entry(frame)
nombre_entry.grid(row=0, column=1)

descripcion_label = ttk.Label(frame, text="Descripción:")
descripcion_label.grid(row=1, column=0)
descripcion_entry = ttk.Entry(frame)
descripcion_entry.grid(row=1, column=1)

precio_label = ttk.Label(frame, text="Precio:")
precio_label.grid(row=2, column=0)
precio_entry = ttk.Entry(frame)
precio_entry.grid(row=2, column=1)

categoria_label = ttk.Label(frame, text="Categoría:")
categoria_label.grid(row=3, column=0)
categorias = ["Comida", "Bebida"]
categoria_combo = ttk.Combobox(frame, values=categorias)
categoria_combo.grid(row=3, column=1)

# Botones
agregar_button = ttk.Button(frame, text="Agregar", command=agregar)
agregar_button.grid(row=4, column=0)
modificar_button = ttk.Button(frame, text="Modificar", command=modificar)
modificar_button.grid(row=4, column=1)
eliminar_button = ttk.Button(frame, text="Eliminar", command=eliminar)
eliminar_button.grid(row=4, column=2)
sin_stock_button = ttk.Button(frame, text="Productos sin Stock", command=mostrar_sin_stock)
sin_stock_button.grid(row=8, column=0)


# Listar productos
lista = tk.StringVar()
productos_listbox = tk.Listbox(frame, listvariable=lista, width=40)
productos_listbox.grid(row=5, column=0, columnspan=3)

listar_productos()

# Resultado
resultado = tk.StringVar()
resultado_label = ttk.Label(frame, textvariable=resultado)
resultado_label.grid(row=6, column=0, columnspan=3)

# ID para modificar/eliminar
menu_id_label = ttk.Label(frame, text="ID:")
menu_id_label.grid(row=7, column=0)
menu_id_entry = ttk.Entry(frame)
menu_id_entry.grid(row=7, column=1)

root.mainloop()
