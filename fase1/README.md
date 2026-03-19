# Aurora Siger — Análise de Telemetria Pré-Decolagem

Análise de N leituras de telemetria do sistema pré-decolagem da espaçonave Aurora Siger, validando parâmetros operacionais contra requisitos de segurança e aplicando regressão logística para classificação de risco.

---

## Organização

```
fase1/
├── codes/        # código de cada integrante
├── referencias/  # arquivos, exemplos e imagens de referência
└── relatorio/    # relatório final em PDF
```

---

## O que o notebook faz

- Gera N leituras simuladas de telemetria 
- Classifica cada leitura como **PRONTO PARA DECOLAR** ou **DECOLAGEM ABORTADA**
- Registra quais parâmetros causaram cada falha
- Calcula autonomia energética disponível para a decolagem
- Aplica regressão logística para análise probabilística de risco

---

## Parâmetros de Segurança

| Parâmetro | Faixa Segura |
|---|---|
| Temperatura interna | 15 – 30 °C |
| Temperatura externa | -20 – 40 °C |
| Integridade estrutural | 1 |
| Nível de energia | ≥ 80% |
| Pressão dos tanques | 3 – 5 bar |
| Módulo de navegação | 1 |
| Módulo de comunicação | 1 |
| Módulo de propulsão | 1 |

---

## Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/computer_science_fiap.git
cd computer_science_fiap/fase1
```

**2. Crie e ative o ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Abra o notebook**
```bash
jupyter notebook
```

---

## Dependências

```
numpy
pandas
matplotlib
seaborn
scikit-learn
jupyter
```