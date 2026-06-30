import random
import time

#Lo de acá es para que el jugador no pueda poner cualquier cosa y el juego se rompa.

def verfic_comando(comando):
        while comando not in ["a", "b", "c"]:
          print("Opción incorrecta. Volvé a intentarlo") #Que diga 'volve' y no 'vuelve' es ejemplo de lo dicho abajo.
          comando = input("> ").strip().lower()


def jugar():
    

#Primeros textos del juego empiezan aca.

#Me parece importante destacar las voces narrativas y las expresiones usadas, 
#considerando que la trama se ubica en Formosa.

#Tanto el sujeto narrativo de la historia, como el texto que es mostrado al usuario, deben mantener coherencia.
#(ver ejemplo comentario linea '8')

    time.sleep(3) #Todo este texto siguiente queda por pruebas, pero es a revisar.
    print("...cuantas cosas han pasado en el último año...")
    time.sleep(2)
    print("... la mente de las personas no fué la misma desde que el proyecto oficialmente inicio... ")
        #Averiguar como espaciar texto. Calibrar textos y tiempo de lectura.
    time.sleep(2)
    print("Es curioso, el humano se creé libre, pero sus acciones ya están dictadas")

    time.sleep(2)
    print("... es el precio por matar a Dios...")

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
             
#Ahora deberia desarrollarse las continuaciones de cada una de las decisiones.
  
# Ejecutar el juego
if __name__ == "__main__":
    jugar()