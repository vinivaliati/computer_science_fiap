# DADOS DA NAVE AURORA SIGER
# temp_interna: 30
# temp_interna: -15
# integridade: 1 para OK e 0 para Falha
# energia: 0 a 100%
# pressao: 3 and 5
# modulos: OK ou ERRO

print("--- SISTEMA DE PRÉ-LANÇAMENTO ---")

# Dados
temp_interna = float(input("Digite a temperatura interna (°C): "))
temp_externa = -float(input("Digite a temperatura externa (°C): "))
integridade = int(input("Integridade do casco (1 para OK, 0 para Falha): "))
energia = float(input("Nível de energia atual (0 a 100%): "))
pressao = float(input("Pressão atmosférica (atm): "))
modulos = input("Status dos módulos (Digite 'OK' ou 'ERRO'): ")

# Verificacao
if (
    15 <= temp_interna <= 30 and
    energia >= 80 and
    integridade == 1 and
    3 <= pressao <= 5 and
    modulos == "OK"
):

    print("PRONTO PARA DECOLAR ✔")
else:
    print("DECOLAGEM ABORTADA ❌")

# Analise Energetica
capacidade_total = 1500 # kWh
consumo_decolagem = 750 # kWh
perda_percentual = 0.08

energia_disponivel = capacidade_total * (energia / 100)
perdas = energia_disponivel * perda_percentual
energia_real = energia_disponivel - perdas

print("Energia real:", energia_real, "kWh")

if energia_real >= consumo_decolagem:
    print("Autonomia suficiente para a decolagem.")
else:
    print("Autonomia insuficiente para a decolagem.")
