import bd_connect, getpass
conexion = bd_connect.db()
cursor = conexion.cursor()


def registroUser():
        try:
            print("---Registrate---")
            email= input("Email: ").strip()
            password= getpass.getpass("Contraseña: ").strip()

            cursor.execute("INSERT INTO clientes (correo, contrasela) VALUES (%s, %s)", (email, password))
            conexion.commit()
            print("Usuario registrado correctamente.")

        except:
            print("\n--Usuario ya Existente--")
            redireccion= int(input("Si deseas iniciar sesion introduzca 1 || Si deseas seguir en el registro introduzca 2: "))
            if redireccion == 1:
                inicioSesion()
            else:
                registroUser()

def inicioSesion():
    try:
        while True:
            print("\n--Inicio de Sesion--")
            email= input("Email: ").strip()
            password= getpass.getpass("Contraseña: ").strip()
            password_db=cursor.execute("SELECT contrasela from clientes where correo = %s", (email,))
            resultado= cursor.fetchone()
            password_db =resultado[0]

            if password == password_db:
                print("Sesion Iniciada Correctamente")
                return email, password; break
            
            else:
                print("--Contraseña incorrecta. Intentalo de nuevo--")
    except:
        print("\n--El usuario NO existe--")
        redireccion= int(input("Si deseas Registrarte introduzca 1 || Si deseas seguir en el proceso introduzca 2: "))
        if redireccion == 1:
            registroUser()
        else:
            inicioSesion()

def leerCatalogo():
    cursor.execute("Select * from categorias")
    resultado = cursor.fetchall()

    print("\n---Catalogo de Categorias---")
    for numero, categoria in resultado:
        print(f"{numero}.- {categoria}")

    user_input=int(input("Que categoria deseas ver?: "))

    cursor.execute("SELECT nombreProducto, precio, stock FROM productos WHERE idCategoria = %s", (user_input,))
    resultado = cursor.fetchall()
    for nombre, precio, stock in resultado:
        print(f"Producto: {nombre} || Precio: {precio} || Stock: {stock}")