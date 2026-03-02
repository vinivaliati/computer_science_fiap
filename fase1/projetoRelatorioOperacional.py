# Dados
temp_interna = 30
temp_externa = -15
integridade = 1
energia = 100
pressao = 4
modulos = "OK"

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