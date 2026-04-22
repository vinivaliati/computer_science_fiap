"""
MGPEB - Modulo De Gerenciamento de Pousos
"""

# Estruturas Lineares, Lista Geral, Fila de espera e pilha de emergencia
espaconave  =  [] 
fila       =  []
emergencia =  []

# Cadastro
def cadastrar (codigo, tipo, combustivel, prioridade, co2):
    """Cria registro da espaçonave e insere na lista e na fila"""
    av = {"cod": codigo, "tipo": tipo, "comb": combustivel,
          "prior": prioridade, "co2": co2, "ok": False}
    espaconave.append(av)
    fila.append(av)
    print(f" [+] {codigo} cadastrada")


# Portas Logicas e Funcoes que simulam And, OR e not 
AND = lambda a, b: a and b
OR = lambda a, b: a or b
NOT = lambda a: not a


# Autorizacao if, elif, else
def autorizar(av, pista_livre):
    """Decide o pouso usando funcoes booleanas e estruturas condicionais"""
    critico = av["comb"] <= 15 # combustivel critico?
    medica  = av["tipo"] == "medica" # carga medica?
    prior1  = av["prior"] == 1 # prioridade max?

    if AND(critico, pista_livre): # AND > Emergencia
        return True, "Emergencia: combustivel critico ?"
    elif AND(OR(medica, prior1), pista_livre):
        return True, "Carga medica / Prioridade maxima"
    elif NOT(pista_livre):
        return False, "Pista ocupada"