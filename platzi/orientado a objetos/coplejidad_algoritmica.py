# Clases de complejidad algorítmica
# Existen distintos tipos de complejidad algorítmica:

# O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
# O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
# O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
# O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
# O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
# O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
# O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.

#o(1) de manera constante no varia el tiempo dejejcutarse 
#o(n) lineal si va creciento el imput 10 entonces 10 veces mas , entonces a medida que crece imput de forna lineal
#o(log n) logaritmica crece pero entre mas datos va creciendo de una menera pequeña
#0(n log n) log lineal
#o(n**2) Polinomial
#0(2**n) expotencial


def Esprimo(n):
    x=2
    for (x=2;x*x<=n;x++):
        if(n%x==0):
            return False;
    
    return True