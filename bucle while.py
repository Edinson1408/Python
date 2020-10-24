numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero=int(input("Escribe tu numero"))

while numeroSecreto!=numero:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!" )
    numero=int(input("Escribe tu numero"))
    
    
print("¡Bien hecho, muggle! Eres libre ahora" )
    