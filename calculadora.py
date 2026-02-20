#Calculadora# 
def sumar (a, b): 
    resultado = a + b
    return resultado
def calcular_promedio(numeros):
    total = 0
    for numero in numeros: 
        total= total + numero
    promedio = total / len(numeros)
    return promedio
#Programa principal# 
num1 = 10
num2 = 5

suma = sumar(num1, num2)
print("La suma es:", suma)

lista_numeros = [10,20,30,40,50]
promedio = calcular_promedio(lista_numeros)
print("El promedio es:", promedio)
