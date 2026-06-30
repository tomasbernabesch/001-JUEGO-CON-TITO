import random
import time

#Lo de acá es para que el jugador no pueda poner cualquier cosa y el juego se rompa.

def reproducir_intro():
   #Todo este texto siguiente queda por pruebas, pero es a revisar.
    print("...cuantas cosas han pasado en el último año...")
        
    print("... la mente de las personas no fué la misma desde que el proyecto oficialmente inicio... ")
        #Averiguar como espaciar texto. Calibrar textos y tiempo de lectura.
 
    print("Es curioso, el humano se creé libre, pero sus acciones ya están dictadas")

    #time.sleep(1)
    print("... es el precio por matar a Dios...")

    #time.sleep(1)
    print(" Estás en el medio de la noche caminando hacía tu casa")

    #time.sleep(1)
    print("Estas un poco cansado, fue un dia largo... ")

    #time.sleep(1)
    print("Ves acercandose a alguien. El rostro te suena familiar pero no logras recordar de donde")
    
    #time.sleep(1)
    print("¿Que decidis?") 

    #time.sleep(1)
    print("a. Te detenes y lo saludas")
    print("b. Pensas ""Creo que no me vío"" tratando de esquivarlo")
    print("c. Cambias de dirección")

def pedir_comando():
    comando = input("> ").strip().lower()
    return verfic_comando(comando)
     

def verfic_comando(comando):
        while comando not in ["a", "b", "c"]:
          print("Opción incorrecta. Volvé a intentarlo") #Que diga 'volve' y no 'vuelve' es ejemplo de lo dicho abajo.
          comando = input("> ").strip().lower()
        return comando


def jugar():
    comando = "a"
    reproducir_intro()
    comando = pedir_comando()

 #CAMINO 1.0:
    if comando == "a":
        #time.sleep(1)
        print("La situación se vuelve incomoda. Ël no parece recordarte de ningún lado.")
        ##time.sleep(1)
        print("EXTRAÑO:- Compa, ni te juno. Raja de acá o te hago boleta")   
        #time.sleep(1)
        print("... ")
        #time.sleep(1)
        print("pasa algo re loco hay narracion flashera")
        #dafasdfasdfsad pritnt con "fsdafasdfasd"
        comando = pedir_comando()

        # CAMINO 1.1 a
        if comando == "a":
          #time.sleep(1)
          print("Lacddd.")
          print(" gavbafbasdfdsa")
          # CAMINO 1.1 b
        else :
          #time.sleep(1)
          print("Dee.")

                        























# CAMINO 2.0: 
    elif comando == "b":
            time.sleep(1)
            print("Pasas de largo a su lado.")
# CAMINO 3.0:
    elif comando == "c":
             time.sleep(1)
             print("Doblas a la izquierda")
             
#Ahora deberia desarrollarse las continuaciones de cada una de las decisiones.
  

if __name__ == "__main__":
    jugar()