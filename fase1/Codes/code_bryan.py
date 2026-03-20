# Bryan Lima Garcia - TURMA: CCOC
# Projeto Aurora Siger
# Relatório de Pré Decolagem

import os

# entrada de dados

def coletar_dados():
    print("\n➡ INSIRA OS DADOS DA TELEMETRIA ⬅\n")

    dados = {
        "temp_interna": float(input("Temperatura interna (°C): ")),
        "temp_externa": float(input("Temperatura externa (°C): ")),
        "integridade": int(input("Integridade do casco (1 OK / 0 Falha): ")),
        "energia": float(input("Nível de energia (%): ")),
        "pressao": float(input("Pressão dos tanques (bar): ")),
        "mod_navegacao": int(input("Módulo de navegação (1 OK / 0 Falha): ")),
        "mod_comunicacao": int(input("Módulo de comunicação (1 OK / 0 Falha): ")),
        "mod_propulsao": int(input("Módulo de propulsão (1 OK / 0 Falha): "))
    }

    return dados


# verificação operacional

def verificar_decolagem(dados):
    if dados["integridade"] == 0:
        return "❌ ABORTADA: Falha estrutural"
    
    if dados["energia"] < 70:
        return "❌ ABORTADA: Energia insuficiente"
    
    if dados["pressao"] < 200 or dados["pressao"] > 230:
        return "❌ ABORTADA: Pressão fora do limite"
    
    if dados["mod_navegacao"] == 0:
        return "❌ ABORTADA: Navegação inoperante"
    
    if dados["mod_comunicacao"] == 0:
        return "❌ ABORTADA: Comunicação inoperante"
    
    if dados["mod_propulsao"] == 0:
        return "❌ ABORTADA: Propulsão inoperante"
    
    return "✅ SISTEMAS OK"


# análise energética

def analise_energetica(energia):
    capacidade_total = 1500  # kWh
    consumo_decolagem = 700  # kWh
    perda_percentual = 0.08

    energia_disponivel = capacidade_total * (energia / 100)
    perdas = energia_disponivel * perda_percentual
    energia_real = energia_disponivel - perdas

    print("\n⚡︎ ANÁLISE ENERGÉTICA ⚡︎")
    print(f"Energia disponível: {energia_disponivel:.2f} kWh")
    print(f"Perdas estimadas: {perdas:.2f} kWh")
    print(f"Energia real: {energia_real:.2f} kWh")

    if energia_real >= consumo_decolagem:
        print("✅ Autonomia SUFICIENTE para a decolagem")
        return True
    else:
        print("❌ Autonomia INSUFICIENTE para a decolagem")
        return False


# ia simples para classificação de risco

def analise_ia(dados):
    risco = 0

    if dados["energia"] < 85:
        risco += 0.4

    if dados["pressao"] < 205 or dados["pressao"] > 225:
        risco += 0.3

    if dados["temp_interna"] < 15 or dados["temp_interna"] > 30:
        risco += 0.3


    print("\n・ ANÁLISE POR IA ・")

    if risco >= 0.5:
        print("⚠️ Risco MODERADO detectado")
        return False
    else:
        print("✅ Risco BAIXO")
        return True


# sistema principal

def main():
    os.system('cls')
    print(".✦ ݁˖ SISTEMA AURORA SIGER INICIADO... .✦ ݁˖")

    dados = coletar_dados()

    print("\n⋆ VERIFICAÇÃO OPERACIONAL ⋆")
    status = verificar_decolagem(dados)
    print("Status:", status)

    energia_ok = analise_energetica(dados["energia"])
    risco_ok = analise_ia(dados)

    print("\n✦ RESULTADO FINAL ✦")

    if "ABORTADA" in status or not energia_ok:
        print("❌ DECOLAGEM ABORTADA!! ❌")
    else:
        print("✅ PRONTO PARA DECOLAR!! ✅")


#execução

if __name__ == "__main__":
    main()