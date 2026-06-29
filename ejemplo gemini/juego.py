import random
import time

def jugar():
    print("=========================================")
    print(" ¡BIENVENIDO A LA MAZMORRA DE LA CMD! ")
    print("=========================================")
    print("Te encuentras frente a un trasgo oscuro. ¿Qué deseas hacer?")
    print("Hola tito")
    print("Dale boca")
    
    # Estado inicial del enemigo
    vida_enemigo = 20
    
    # Bucle del juego (se repite hasta que ganes o salgas)
    while vida_enemigo > 0:
        print(f"\n[Trasgo - Vida: {vida_enemigo}]")
        print("Comandos disponibles: ATACAR | USAR POCION | HUIR")
        
        # 1. Entrada del usuario
        comando = input("> ").strip().upper()
        
        # 2. Lógica y Resultados Aleatorios
        if comando == "ATACAR":
            print("[Generando...] Lanzando dado de acción...")
            time.sleep(1) # Un pequeño retraso para darle suspenso
            
            # Simulamos un dado de 20 caras (D20)
            dado = random.randint(1, 20)
            print(f"-> Sacaste un: {dado}")
            
            if dado > 10: # ÉXITO
                daño = random.randint(4, 10)
                vida_enemigo -= daño
                print(f"¡ÉXITO! Golpeas al trasgo por {daño} de daño.")
            else: # FALLO
                print("¡FALLO! Tu ataque pasa rozando el aire. El trasgo se burla de ti.")
                
        elif comando == "USAR POCION":
            print("Bebes una poción misteriosa...")
            # Un resultado aleatorio con efectos distintos
            efecto = random.choice(["curacion", "veneno", "nada"])
            if efecto == "curacion":
                print("Te sientes genial. Recuperas energía.")
            elif efecto == "veneno":
                print("¡Oh no! La poción estaba rancia. Pierdes un turno mareado.")
            else:
                print("La poción sabía a agua pura. No pasa nada.")
                
        elif comando == "HUIR":
            print("Corres cobardemente hacia la salida. ¡Fin del juego!")
            time.sleep(10)
            break
        else:
            print("Comando no reconocido. Intenta de nuevo.")
            
        # Comprobar si el enemigo derrotado
        if vida_enemigo <= 0:
            print("\n¡Felicidades! Has derrotado al trasgo y asegurado tu botín.")

# Ejecutar el juego
if __name__ == "__main__":
    jugar()