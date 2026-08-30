import math  # Módulo matemático: necesario para calcular logaritmos en base 2 (math.log2).
import os  # Módulo del sistema operativo: se usa para verificar si existen archivos en el disco duro.
import re  # Módulo de Expresiones Regulares: permite buscar patrones específicos en texto.
from getpass import getpass # Función de terminal: permite solicitar datos sensibles ocultando la entrada.

# Conjunto de reserva (Fallback).
COMMON_PASSWORDS_SET = {
    "123456", "password", "123456789", "12345678", "12345", "qwerty",
    "1234567", "dragon", "pussy", "baseball", "football", "letmein",
    "master", "monkey", "shadow", "sunshine", "123123", "admin",
}

def load_wordlist(filepath="rockyou.txt"):
    """Carga la lista de contraseñas conocidas desde un archivo plano a la memoria RAM."""
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return {line.strip().lower() for line in f}
    return COMMON_PASSWORDS_SET

def calculate_entropy(password):
    """Calcula la entropía de la información de la contraseña en bits."""
    pool_size = 0  
    if re.search(r"[a-z]", password):
        pool_size += 26
    if re.search(r"[A-Z]", password):
        pool_size += 26
    if re.search(r"\d", password):
        pool_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool_size += 32

    if pool_size == 0 or len(password) == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def check_password_strength(password, wordlist):
    """Analiza la estructura de la contraseña y determina su resistencia global."""
    feedback = []

    if password.lower() in wordlist:
        return {
            "is_blacklisted": True,  
            "score": 0,  
            "entropy": calculate_entropy(password), 
            "feedback": ["La contraseña está presente en listas de filtraciones comunes (Wordlist)."],
        }

    score = 0  

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Aumenta la longitud a mínimo 12 caracteres.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Mezcla letras mayúsculas y minúsculas.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Incluye al menos un número.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Incluye al menos un carácter especial.")

    entropy = calculate_entropy(password)

    return {
        "is_blacklisted": False,
        "score": score,
        "entropy": entropy,
        "feedback": feedback,
    }

# Punto de entrada estándar de Python
if __name__ == "__main__":
    print("=== Evaluador de Fuerza de Contraseñas ===")
    
    # Cargamos la wordlist UNA VEZ antes del bucle para no consumir RAM innecesaria en cada intento
    print("[*] Cargando diccionarios de contraseñas...")
    wordlist_en_memoria = load_wordlist("rockyou.txt")
    print("[*] ¡Sistema listo!")

    try:
        while True:
            print("\n" + "-"*40)
            
            # Solo usamos getpass() porque así lo definimos en la línea 4
            password = getpass("Introduce la contraseña (o typea 'quit' para salir): ")

            if password.lower() in ['quit', 'exit', 'q']:
                print("\nSaliendo del evaluador...")
                break
            
            if not password:
                print("No ingresaste ninguna contraseña. Intenta de nuevo.")
                continue

            # Llamamos a tu función correcta pasándole la palabra y el diccionario
            result = check_password_strength(password, wordlist_en_memoria)
            
            # Formateamos la impresión de resultados (lo que antes era tu función main)
            print("\n--- Resultados ---")
            print(f"Entropía estimada: {result['entropy']} bits")

            if result["is_blacklisted"] or result["entropy"] < 36:
                print("Calificación: Débil")
            elif result["entropy"] < 60:
                print("Calificación: Moderada")
            else:
                print("Calificación: Fuerte")

            if result["feedback"]:
                print("\nRecomendaciones para mejorar:")
                for tip in result["feedback"]:
                    print(f"- {tip}")

    except KeyboardInterrupt:
        print("\n\nCierre forzado detectado. Saliendo del sistema...")