"""
MGPEB - Modulo De Gerenciamento de Pousos
"""

# Estruturas Lineares, Lista Geral, Fila de espera e pilha de emergencia
modulos    = []   # lista geral de todos os modulos cadastrados
fila_pouso = []   # fila de pouso FIFO (ordem de chegada a órbita)
pilha_emer = []   # pilha de emergência LIFO (modulos criticos primeiro)

# Cadastro dos modulos
def cadastrar(nome, tipo, prioridade, combustivel, massa_ton, criticidade, horario_orbita):
    """Cadastra um modulo da espaçonave e insere na lista e na fila

        Atributos:
        nome (str): Identificador do modulo
        tipo (str): Habitacao, Energia, Laboratorios, Logistica, Medico
        prioridade (int): 1= alta, 2= media, 3= baixa
        combustivel (int): percentual restante de combustivel (0-10%)
        massa_ton (float): massa do modulo em toneladas(ton)
        criticidade (str): "alta", "media" ou "baixa"
        horario_orbita (str): horario estimado de chegada a orbita (ex: 10:50)

    """

mod = {
       "nome":   nome,
       "tipo":   tipo,
       "prior":  prioridade,
       "comb":   combustivel,
       "massa":  massa_ton,
       "critic": criticidade,
       "orbita": horario_orbita,
       "ok":     False  # Sera definido pela logica de autorizacao

   }
modulos.append(mod)
fila_pouso.append(mod)
print(f"[+] {nome} ({tipo}) - chegada a orbita: {horario_orbita}")



# Portas Logicas e Funcoes que simulam AND, OR e NOT 
AND = lambda a, b: a and b
OR = lambda a, b: a or b
NOT = lambda a: not a


# Autorizacao De pouso usando if, elif, else
def autorizar(mod, pista_livre):
    """Decide a autorizacao de pouso usando funcoes booleanas"""
    comb_critico = mod["comb"] <= 15 # combustivel critico?
    eh_medica  = mod["tipo"] == "medica" # carga medica?
    prior_alta  = mod["prior"] == 1 # prioridade max?
    critic_alta = mod["critic"] == "alta" # carga de alta criticidade

    if AND(comb_critico, pista_livre): # emergencia imediata
        return True, "Emergencia: combustivel critico"
    
    elif AND(OR(eh_medica, critic_alta), pista_livre):
        return True, "Carga medica / criticidade alta, pouso prioritario"
    
    elif NOT(pista_livre):
        return False, "ditch indisponivel, aguardar orbita."
    
    elif mod["comb"] >  30 and mod["prior"] > 2:
        return False, "Combustivel estavel, aguardar na fila"
    
    else:
        return True, "Condicoes normais, pouso liberado"
    

# Busca Linear
def buscar_tipo(tipo):
    """Retorna todas as espaconaves de um determinado tipo de carga"""
    return [m for m in modulos if m["tipo"] == tipo]

def menor_combustivel():
    """Retorna o modulo com menos combustivel (mais critica)"""
    return min(modulos, key=lambda m: m["comb"])

def buscar_criticidade(nivel):
    """Busca modulos por nivel de criticidade da carga"""
    return [m for m in modulos if m["critic"] == nivel ]


# Ordena por combustível crescente
def bubble_sort(lista):
    """Modulos com menos combustivel sobem para o inicio da fila"""
    lst = lista[:]
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j]["comb"] > lst[j+1]["comb"]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# Ordena por prioridade crescente
def selection_sort(lista):
    """Modulos com prioridade 1 (mais urgente) ficam no topo da fila"""
    lst = lista[:]
    for i in range(len(lst)):
        menor = min(range(i, len(lst)), key=lambda j: lst[j]["prior"])
        lst[i], lst[idx] = lst[idx], lst[i]
    return lst


# Pilha de emergencia
def push_emergencia(av):
    """Empilha modulo em emergencia (Push)"""
    pilha_emer.append(mod)
    print(f" [!] EMERGENCIA: {mod['nome']} empilhado para pouso imediato")

    def pop():
        """Desempilha o modulo mais urgente (pop)"""
        return pilha_emer.pop() if pilha_emer else None
    

# Log de autorizacao
def log_status(mod, ok, msg):
    """Exibe o resultado da autorizacao de forma legivel"""
    status = "Ok" if ok else "Erro"
    print(f" [{mod['nome']}] {status} - {msg}")


# Exibicao
def exibir(lista, titulo):
    print(f"\n{'─'*62}\n  {titulo}\n{'─'*62}")
    for m in lista:
        s = "Correto" if m["ok"] else "Esperando"
        print(f"  {s} {m['nome']:14} | {m['tipo']:12} | comb:{m['comb']:3}% "
              f"| prior:{m['prior']} | {m['massa']:5.1f}t | critic:{m['critic']:5} | {m['orbita']}")
        

# Principal
if __name__ == "__main__":

    print("=" * 62)
    print("MGPEB - Missao Espacial Aurora Siger")
    print("Sistema de Gerenciamento de Pouso")
    print("=" * 62)


# Cadastro dos modulos
# Atributos: nome, tipo, prioridade, combustivel(%), massa(toneladas (t), criticidade, horario_orbita
print("\n[1] CADASTRO DOS MODULOS")
cadastrar("MOD-HAB-01,")
