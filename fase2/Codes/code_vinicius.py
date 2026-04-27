# Lista de módulos (fila)
import random

tipos = ["habitação", "energia", "laboratório", "logística", "suporte médico"]
criticidades = ["baixa", "média", "alta"]

modulos = []

for i in range(30):
    modulo = {
        "tipo": random.choice(tipos),
        "prioridade": random.randint(1, 5),
        "combustivel": random.randint(10, 100),
        "massa": random.randint(2000, 6000),
        "criticidade": random.choice(criticidades),
        "horario_chegada": i + 1,
        "status": "em fila"
    }
    modulos.append(modulo)

# Busca linear - menor combustível
def buscar_menor_combustivel(lista):
    menor = lista[0]
    for modulo in lista:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor

# Busca linear - maior prioridade
def buscar_maior_prioridade(lista):
    maior = lista[0]
    for modulo in lista:
        if modulo["prioridade"] > maior["prioridade"]:
            maior = modulo
    return maior

# Bubble sort por prioridade (maior primeiro)
def ordenar_por_prioridade(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["prioridade"] < lista[j + 1]["prioridade"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Simulação de decisão
def simular_pouso(lista):
    sensores_ok = True
    area_disponivel = True
    atmosfera_ok = True

    for modulo in lista:
        combustivel_ok = modulo["combustivel"] > 50
        alerta_combustivel = modulo["combustivel"] < 40
        alta_prioridade = modulo["prioridade"] >= 4

        condicao_base = sensores_ok and area_disponivel

        if (not combustivel_ok) or (not sensores_ok):
            modulo["status"] = "alerta"

        elif condicao_base and alerta_combustivel and alta_prioridade:
            modulo["status"] = "pousado"

        elif condicao_base and combustivel_ok and atmosfera_ok and not alerta_combustivel:
            modulo["status"] = "pousado"

        else:
            modulo["status"] = "espera"

    return lista

# Execução

print("Módulo com menor combustível:")
print(buscar_menor_combustivel(modulos))

print("\nMódulo com maior prioridade:")
print(buscar_maior_prioridade(modulos))

# Se houver alerta, ordena por prioridade
if any(m["combustivel"] < 40 for m in modulos):
    ordenar_por_prioridade(modulos)

print("\nSimulação de pouso:")
resultado = simular_pouso(modulos)

for m in resultado:
    print(m)