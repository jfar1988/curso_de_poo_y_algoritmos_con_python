import random

def busqueda_Lineal(lista, objetivo):
    match = False

    for elemento in lista: #o(n)
        if elemento == objetivo:
            match =True
            break
    return match

if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]  # Nos permite generar numeros aleatorios


    encontrado = busqueda_Lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') # operadores terciarios: podemos generar un if else dentro de una misma linea de codigo
