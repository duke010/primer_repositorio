lista_clientes = []
ancla = -1

class Cliente:


    

    def __init__(self, nombre, edad, dinero):

        def codigeare():
            cant = str(len(lista_clientes) + 1)
            cant2 = 4 - len(cant)
            cant = cant2 * "0" + cant
            return cant

        self.nombre = nombre
        self.edad = edad
        self.dinero = dinero
        self.codigo = codigeare()

        print(f"Se ha creado la cuenta con exito de {nombre} su codigo de cliente es: {self.codigo}.")
        
        

    def __str__(self):
        return f"El cliente {self.nombre}, de {self.edad} anios y con el codigo {self.codigo}, tiene {self.dinero}$." 

    def comprar(self):
        a_pagar = int(input("Ingrese el monto que se debe pagar: "))
        if a_pagar > self.dinero:
            print(f"{self.nombre} no cuenta con el suficiente dinero por lo que no se ejecutara la compra.")
            print(f"Dinero de {self.nombre}: {self.dinero}$.")
        else:
            self.dinero -= a_pagar
            print(f"Se ha ejecutado la compra con exito, {self.nombre} tiene {self.dinero}$ ahora.")
        
    def vender(self):
        a_recibir = int(input("Ingrese el monto que se recibiria: "))
        self.dinero += a_recibir
        print(f"Se ha ajecutado la venta con exito, {self.nombre} tiene {self.dinero}$ ahora.")

    def agregarDinero(self):
        dinero = int(input(f"Ingrese la cantidad de dinero que va a agregar: "))
        self.dinero += dinero
        print(f"{self.nombre} ahora tiene {self.dinero}$")


def registrar():
    nombre = input("Ingrese el nombre del nuevo cliente: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    dinero = int(input(f"Ingrese el dinero con el que ingresa {nombre}: "))
    lista_clientes.append(Cliente(nombre, edad, dinero))
    ancla = len(lista_clientes) - 1
    menu()

def iniciarSesion():
    codigo = input("Ingrese su codigo completo, teniendo en cuenta los ceros a la izquierda en caso de los haya: ")
    confi = False
    for i in range(len(lista_clientes)):
        if lista_clientes[i].codigo == codigo:
            ancla = i
            print(f"Bienvenido a su cuenta {lista_clientes[i].nombre}")
            confi = True
    if not confi:
        print(f"El codigo: {codigo} no pertenece a ninguna cuenta registrada.")
    else:
        menu()


def comprar():
    lista_clientes[ancla].comprar()

def vender():
    lista_clientes[ancla].vender()

def agregar():
        lista_clientes[ancla].agregarDinero()

def menu():
    opc = 0
    while opc < 4:
        print("1. Comprar")
        print("2. Vender")
        print("3. Ingresar dinero")
        print("4. Salir")
        opc = int(input("Ingrese su opcion: "))
        if opc == 1:
            comprar()
        elif opc == 2:
            vender()
        elif opc == 3:
            agregar()

opc = 0
while opc < 3:
    print("1. Registrarse")
    print("2. Iniciar Sesion")
    print("3. Salir")
    opc = int(input("Ingrese su opcion: "))
    if opc == 1:
            registrar()
    elif opc == 2:
            iniciarSesion()


    
    
