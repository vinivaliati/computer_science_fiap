# BRYAN LIMA GARCIA - MGPEB missao aurora siger code
# gerenciamento de pouso em marte

import random
import math

# gerando os modulos com random
# usei random.sample pra garantir variedade nos tipos e criticidades
# e range com step pra massa e combustivel nao ficarem tao aleatorios

tipos = ["habitação", "energia", "laboratório", "logística", "suporte médico"]
criticidades = ["baixa", "média", "alta"]

# gera listas de valores aleatorios separadas
tipos_sorteados = [random.choice(tipos) for _ in range(15)]
prioridades     = [random.randint(1, 5) for _ in range(15)]
combustiveis    = [random.randint(10, 100) for _ in range(15)]
massas          = [random.randint(2000, 6000) for _ in range(15)]
crits_sorteadas = [random.choice(criticidades) for _ in range(15)]

# monta os modulos juntando tudo com zip
modulos = []
for i, (tipo, prio, comb, massa, crit) in enumerate(zip(tipos_sorteados, prioridades, combustiveis, massas, crits_sorteadas)):
    modulo = {
        "id": i + 1,
        "tipo": tipo,
        "prioridade": prio,
        "combustivel": comb,
        "massa": massa,
        "criticidade": crit,
        "horario_chegada": i + 1,
        "status": "em fila"
    }
    modulos.append(modulo)

# estruturas lineares
fila_pouso = list(modulos)  # fila de modulos esperando pousar
pousados = []               # modulos que ja pousaram
em_espera = []              # modulos esperando
pilha_alertas = []          # modulos com problema (pilha)

# busca linear - acha o modulo com menos combustivel
def buscar_menor_combustivel(lista):
    menor = lista[0]
    for modulo in lista:
        if modulo["combustivel"] < menor["combustivel"]:
            menor = modulo
    return menor

# busca linear - acha o modulo mais importante
def buscar_maior_prioridade(lista):
    maior = lista[0]
    for modulo in lista:
        if modulo["prioridade"] > maior["prioridade"]:
            maior = modulo
    return maior

# busca binaria por id (a lista tem que estar ordenada por id)
def busca_binaria_id(lista, id_alvo):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio]["id"] == id_alvo:
            return lista[meio]
        elif lista[meio]["id"] < id_alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

# bubble sort - ordena por prioridade do maior pro menor
def ordenar_por_prioridade(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["prioridade"] < lista[j + 1]["prioridade"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# insertion sort - ordena por horario de chegada
def ordenar_por_chegada(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["horario_chegada"] > chave["horario_chegada"]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

# simulacao de pouso com logica booleana
# se combustivel for baixo ou sensor ruim = alerta
# se for critico mas muito importante = pousa mesmo assim
# se tiver tudo ok = pousa normal
# se nao = espera
def simular_pouso(lista, sensores_ok=True, area_ok=True, atmosfera_ok=True):
    for modulo in lista:
        combustivel_ok = modulo["combustivel"] > 50
        comb_critico = modulo["combustivel"] < 40
        alta_prioridade = modulo["prioridade"] >= 4

        if (not combustivel_ok) or (not sensores_ok):
            modulo["status"] = "alerta"
        elif sensores_ok and area_ok and comb_critico and alta_prioridade:
            modulo["status"] = "pousado"
        elif sensores_ok and area_ok and combustivel_ok and atmosfera_ok:
            modulo["status"] = "pousado"
        else:
            modulo["status"] = "espera"

        if modulo["status"] == "pousado":
            pousados.append(modulo)
        elif modulo["status"] == "espera":
            em_espera.append(modulo)
        else:
            pilha_alertas.append(modulo)  # empilha o alerta

    return lista

# funcoes matematicas do pouso

# altura em funcao do tempo - funcao quadratica
# h(t) = h0 - v0*t - (1/2)*g*t^2
# g de marte é 3.72 m/s2
def altura_descida(t, h0=10000, v0=200, g=3.72):
    h = h0 - v0 * t - 0.5 * g * t ** 2
    if h < 0:
        h = 0
    return h

# consumo de combustivel - funcao quadratica
# C(v) = k * v^2
# dobrar a velocidade faz o consumo quadruplicar
def consumo_combustivel(v, k=0.00002):
    return k * v ** 2

# energia solar ao longo do dia marciano - funcao senoidal
# E(t) = Emax * sen(pi * t / 24.6)
# dia em marte tem 24.6 horas
def energia_solar(t, E_max=15.0):
    if 0 <= t <= 24.6:
        return max(0.0, E_max * math.sin(math.pi * t / 24.6))
    return 0.0

# --- execucao do programa ---

print("=== modulo com menor combustivel (busca linear) ===")
print(buscar_menor_combustivel(modulos))

print("\n=== modulo com maior prioridade (busca linear) ===")
print(buscar_maior_prioridade(modulos))

print("\n=== busca binaria pelo id 5 ===")
lista_ordenada = sorted(modulos, key=lambda m: m["id"])
print(busca_binaria_id(lista_ordenada, 5))

print("\n=== fila ordenada por prioridade (bubble sort) ===")
ordenar_por_prioridade(fila_pouso)
for m in fila_pouso:
    print(f"id {m['id']} | {m['tipo']} | prioridade: {m['prioridade']} | combustivel: {m['combustivel']}%")

print("\n=== fila ordenada por chegada (insertion sort) ===")
ordenar_por_chegada(fila_pouso)
for m in fila_pouso:
    print(f"id {m['id']} | {m['tipo']} | chegada: {m['horario_chegada']}h")

print("\n=== simulacao de pouso ===")
if any(m["combustivel"] < 40 for m in fila_pouso):
    print("aviso: combustivel critico detectado, reordenando por prioridade...")
    ordenar_por_prioridade(fila_pouso)

resultado = simular_pouso(fila_pouso)
for m in resultado:
    print(f"id {m['id']} | {m['tipo']} | prioridade: {m['prioridade']} | combustivel: {m['combustivel']}% | status: {m['status']}")

print(f"\npousados: {len(pousados)} | em espera: {len(em_espera)} | alertas: {len(pilha_alertas)}")

if pilha_alertas:
    topo = pilha_alertas.pop()  # pega o ultimo da pilha (LIFO)
    print(f"modulo no topo da pilha de alertas: id {topo['id']} | {topo['tipo']} | combustivel: {topo['combustivel']}% | status: {topo['status']}")

print("\n=== altura de descida h(t) = 10000 - 200t - 0.5*3.72*t^2 ===")
for t in range(0, 301, 20):
    h = altura_descida(t)
    if 0 < h <= 500:
        print(f"t={t}s  h={h:.1f}m  <- hora de acionar os retrofoguetes!")
    elif h == 0:
        print(f"t={t}s  h={h:.1f}m  <- toque no solo")
        break
    else:
        print(f"t={t}s  h={h:.1f}m")

print("\n=== consumo de combustivel C(v) = 0.00002 * v^2 ===")
for v in [6000, 3000, 1000, 500, 100]:
    print(f"v={v}m/s  consumo={consumo_combustivel(v):.2f}kg/s")
print("obs: dobrar a velocidade faz o consumo ficar 4x maior")

print("\n=== energia solar ao longo do dia marciano ===")
for h in range(0, 25, 2):
    e = energia_solar(h)
    if e >= 8:
        print(f"{h}h  {e:.2f}kW  [pode pousar]")
    else:
        print(f"{h}h  {e:.2f}kW  [sem energia suficiente]")
