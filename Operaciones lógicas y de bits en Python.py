#17 // 2 → 8 (desplazarse hacia la derecha en un bit equivale a la división de enteros en dos)
#17 * 4 → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro).

var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)
