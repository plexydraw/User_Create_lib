import random
import string
import json

class Crear_User:
    def __init__(self) -> None:
        pass

    def Obtener_Nombre():
        with open('Nombres.txt', 'r') as archivo:
            lineas = archivo.readlines()
    
        seleccion = random.randint(0, len(lineas) -1)
        nombre = lineas[seleccion]
        f_nombre = nombre.rstrip('\n')
            
        return f_nombre

    def Obtener_Apellido():
        with open('Apellidos.txt', 'r') as archivo:
            lineas = archivo.readlines()
    
        seleccion = random.randint(0, len(lineas) -1)
        apellido = lineas[seleccion]
        f_apellido = apellido.rstrip('\n')
            
        return f_apellido
    
    def Obtener_Fecha_Nacimiento():
        dia = random.randint(1,30)
        mes = random.randint(1,12)
        año = random.randint(1920, 2005)

        fecha = f"{dia}/{mes}/{año}"

        return fecha

    def Craar_Tag(Nombre):
        terminaciones = [
            "YT","Gamer","Plays","TV","Official","Stream","Live","Vlogs","Clips","Zone","Craft","X","Ninja","Master","Tech","Guru","Pro","Vibe"
        ]
        Numero = random.randint(20,2024)
        seleccion = random.randint(0, len(terminaciones) -1)
        arg = terminaciones[seleccion]
        Tag = f"{Nombre}_{Numero}_{arg}"

        return Tag

    def Crear_Password(usuario):
        while True:
            mayuscula = random.choice(string.ascii_uppercase)
            minusculas = ''.join(random.choices(string.ascii_lowercase, k=5))
            numero = random.choice(string.digits)
            caracter_especial = random.choice('!@#$%^&*()-_=+[]{}|;:,.<>?')
            contrasena = mayuscula + minusculas + numero + caracter_especial
            contrasena = ''.join(random.sample(contrasena, len(contrasena)))
            if len(contrasena) < 8:
                contrasena += ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%^&*()-_=+[]{}|;:,.<>?', k=8-len(contrasena)))
            if (usuario.lower() not in contrasena.lower() and
                'twitch' not in contrasena.lower() and
                'aaa' not in contrasena.lower() and
                '123' not in contrasena.lower()):

                return contrasena
            
    def Almacenar_User(user):
        try: 
            data_str = json.dumps(user, ensure_ascii=False)
            with open("Cuentas.txt", 'a') as file:
                file.write(data_str + '\n')  
        except IOError as e:
            print(f"Ocurrió un error al escribir en el archivo: {e}")


    def Obtener_User_completo():

        Nombre = Crear_User.Obtener_Nombre()
        Apellido = Crear_User.Obtener_Apellido()
        Tag = Crear_User.Craar_Tag(Nombre)
        Password = Crear_User.Crear_Password(Tag)
        Fecha = Crear_User.Obtener_Fecha_Nacimiento()
    
        usuario = {

            "Nombre" : Nombre,
            "Apellido" : Apellido,
            "Fecha" : Fecha,
            "Tag" : Tag,
            "Password" : Password,

        }

        Crear_User.Almacenar_User(usuario)
    
        return usuario
    






        

    