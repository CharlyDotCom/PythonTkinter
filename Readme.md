# Python y Tkinter
## Objetivo
Realizar una aplicación funcional con formulario y almacenamiento de datos en SQLite.

## Video de Faztweb [https://www.youtube.com/watch?v=W2kAF9pKPPE]
Vamos a crear una aplicación de escritorio usando python, y para ello usaremos la biblioteca Tkinter [https://docs.python.org/es/3/library/tkinter.html], que maneja objetos de interfaz de escritorio.
Vamos a integrarlo con una base de datos SQLite [https://www.sqlite.org/index.html], porque es muy simple de instalar.
Usaremos DB Browser [https://sqlitebrowser.org/] para consultar la base de datos.

La aplicación va a gestionar una colección de productos,nombre y precio; y podremos agregar, modificar, consultar y borrar datos (CRUD)
utilizaremos el paradigma de orientación a objetos para crear una clase Producto que controla el formulario 


## Elementos del proyecto 
1. Creamos una carpeta llamada PythonTkinter
2. Creamos un archivo que arranque la aplicación [index.py]
3. Utilizaremos dos bibliotecas: tkinter y sqlite3
4. Creamos una clase Product que contiene el formulario y la logica de negocio
5. Definimos una función __init__ que inicializa el formulario y los datos
6. Definimos en la clase las siguientes funciones:
   1. run_query() => ejecuta sentencias SQL en el base de datos
   2. get_products() => consulta todos los productos de la base de datos 
   3. validation() => valida el contenido de los campos del formulario
   4. add_product() => añade un producto a la base de datos
   5. delete_product() => elimina un producto de la base de datos
   6. edit_product() => Crea un formulario para editar el producto
   7. edit_records() => Modifica un producto en la base de datos
   

