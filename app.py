"""
Laboratorio de Cloud Computing - GitHub Actions
Contribuidores: Jean Marco, Byron Tobar, Osmar Ramírez
"""

import datetime

def saludar():
    """Función de saludo creada por Osmar Ramírez"""
    print('Hola desde mi rama new-feature!')
    print('¡Mejora agregada por Osmar Ramírez!')
    return "Saludo completado"

def mostrar_info():
    """Información del proyecto - Osmar Ramírez"""
    print("=" * 40)
    print("LABORATORIO: GitHub y GitHub Actions")
    print("CURSO: Cloud Computing")
    print("COLABORADOR: Osmar Ramírez")
    print("=" * 40)

def mostrar_fecha_hora():
    """Función para mostrar fecha y hora actual - Byron Tobar"""
    ahora = datetime.datetime.now()
    print(f"Fecha y hora de ejecución: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Función creada por: Byron Tobar")

def calcular_factorial(n=5):
    """Calcula factorial de un número - Byron Tobar"""
    if n <= 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    print(f"El factorial de {n} es: {resultado} (calculado por Byron Tobar)")
    return resultado

if __name__ == "__main__":
    mostrar_info()
    resultado = saludar()
    print(f"Status: {resultado}")
    
    # Nuevas funciones
    print("\n" + "="*50)
    print("NUEVAS FUNCIONALIDADES - BYRON TOBAR")
    print("="*50)
    mostrar_fecha_hora()
    calcular_factorial()
    
    print("\n¡Laboratorio completado exitosamente por el equipo!")
