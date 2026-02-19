class CuentaBancaria:

    # -------------------------------
    # CONSTRUCTOR
    # Se ejecuta al crear el objeto
    # Inicializa los atributos
    # -------------------------------
    def __init__(self, titular,numerocuenta):

        # ATRIBUTO:
        self.titular= titular

        # ATRIBUTO:
        self.numerocuenta= numerocuenta

        # ATRIBUTO:
        self.saldo= 0
        


    # --------- FUNCIONES / MÉTODOS ---------

    def depositar(self, monto):
        self.saldo += monto
        
        print("deposito realizado correctamente")

    def retirar(self, monto):
       if monto <= self.saldo:
           self.saldo-=monto
           print("retiro realizado correctamente")
       else:
           print("saldo insuficiente")
       
    def mostrar_inf(self):
       
        print(f"Titular: {self.titular}")
        print(f"Numero de cuenta: {self.numerocuenta}")
        print(f"Saldo: {self.saldo}")


    # --------- MENÚ ---------

    def menu(self):
        print("¿Qué deseas hacer?")
        print("1. Gastarlo todo en fiestas")
        print("2. Invertir una parte")
        print("3. Ahorrar")

        
    def crear_cuenta():
        cuentas=[]
        titular = input("ingrese nombre del titular: ")
        numero = input("ingrese numero de la cuenta: ")
        saldo = input("ingrese saldo inicial: ")
        nueva_cuenta=CuentaBancaria(titular,numero,saldo)
        cuentas.append(nueva_cuenta)
        print("cuenta creada correctamente")
    
    def mostrar_cuentas():
       for cuentas in cuentas:
           cuentas.mostrar_info()
           print("---------------------------")

    def realizar_deposito():
        numero=input("ingresar numero de la cuenta")
        for cuentas in cuentas:
            if cuentas.numero ==numero:
                monto= float(input("ingrese el monto"))
                cuentas.depostar(monto)
                return
        print("cuenta no existe")
           
    # --------- BUCLE PRINCIPAL ---------

while true:

    print("\n1. CREAR CUENTA")
    print("2. MOSTRAR CUENTAS")
    print("3. DEPOSITAR DINERO")
    print("4. RETIRAR DINERO")
    print("5. SALIR")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        mostrar_cuenta()
    elif opcion == "3":
        realizar_deposito()
    elif opcion == "4":
        reirar_dinero()
    elif opcion == "5":
        print("Saliendo del sistema")
        break
    else:
        print("Opción inválida")


