"""
MGPEB - Modulo De Gerenciamento de Pousos
"""

# Estruturas Lineares, Lista Geral, Fila de espera e pilha de emergencia
espaconave =  [] 
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
        return False, "ditch/pista ocupada"
    elif av["comb"] >  30 and av["prior"] > 2:
        return False, "Aguardar na fila"
    else:
        return True, "Condicoes normais"
    

# Busca Linear
def buscar_tipo(tipo):
    """Retorna todas as espaconaves de um determinado tipo de carga"""
    return [av for av in espaconave if av["tipo"] == tipo]

def menor_combustivel():
    """Retorna a espaconave com menos combustivel (mais critica)"""
    return min(espaconave, key=lambda av: av["comb"])


# Ordena por combustível crescente
def bubble_sort(lista):
    """espaconaves com menos combustivel sobem para o inicio da fila"""
    lst = lista[:]
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j]["comb"] > lst[j+1]["comb"]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# Ordena por prioridade crescente
def selection_sort(lista):
    """espaconaves com prioridade 1 (mais urgente) ficam no topo da fila"""
    lst = lista[:]
    for i in range(len(lst)):
        menor = min(range(i, len(lst)), key=lambda j: lst[j]["prior"])
        lst[i], lst[menor] = lst[menor], lst[i]
    return lst


# Pilha de emergencia
def push_emergencia(av):
    emergencia.append(av)
    print(f" [!] EMERGENCIA: {av['cod']} empilhada")

    def pop_emergencia():
        return emergencia.pop() if emergencia else None
    

# Exibicao
def exibir(lista, titulo):
    print(f"\n{'─'*55}\n  {titulo}\n{'─'*55}")
    for av in lista:
        s = "Correto" if av["ok"] else "Esperando"
        print(f"  {s} {av['cod']:6} | {av['tipo']:12} | comb:{av['comb']:3}% "
              f"| prior:{av['prior']} | CO₂:{av['co2']:.0f}kg")