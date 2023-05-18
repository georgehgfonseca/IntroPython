def encontra_min_max(elementos):
    min = elementos[0] # ou float("inf") para inicializar com infinito
    max = elementos[0] # ou float("-inf") para inicializar com -infinito
    for elemento in elementos:
        if elemento < min:
            min = elemento
        if elemento > max:
            max = elemento
    return (min, max)

def soma_elementos(elementos):
    soma = 0
    for elemento in elementos:
        soma += elemento
    return soma
