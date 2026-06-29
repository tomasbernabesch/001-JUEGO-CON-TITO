import random
import time

def verfic_comando(comando):
        while comando not in ["a", "b", "c"]:
          print("Opción incorrecta. Vuelve a intentarlo")
          comando = input("> ").strip().lower()


def jugar():
    time.sleep(2)
    print("=========================================")
    print(" ¡BIENVENIDO ! ")
    print("=========================================")

    time.sleep(5)
    print(" Estás en el medio de la noche caminando hacía tu casa")

    time.sleep(5)
    print("Estas un poco cansado, fue un dia largo... ")

    time.sleep(3)
    print("Ves acercandose a alguien. El rostro te suena familiar pero no logras recordar de donde")
    
    time.sleep(1)
    print("¿Que decidis?") 

    time.sleep(1)
    print("a. Te detenes y lo saludas")
    print("b. Pensas ""Creo que no me vío"" tratando de esquivarlo")
    print("c. Cambias de dirección")

    comando = input("> ").strip().lower()
    verfic_comando(comando)

    if comando == "a":
            time.sleep(2)
            print("La situación se vuelve incomoda. Ël no parece recordarte de ningún lado.")
            time.sleep(2)
            print("Compa, ni te juno. Raja de acá o te hago boleta")   
            time.sleep(2)
            print("")

    elif comando == "b":
            time.sleep(2)
            print("Pasas de largo a su lado.")

    elif comando == "c":
             time.sleep(2)
             print("Doblas a la izquierda")
             

  
# Ejecutar el juego
if __name__ == "__main__":
    jugar()