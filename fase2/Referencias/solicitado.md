# 1. ATIVIDADE INTEGRADORA – Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)

Nesta fase, as equipes deverão projetar e documentar um **Módulo de Gerenciamento de Pouso e Estabilização de Base (MGPEB)** para a missão Aurora Siger.

O objetivo é simular, de forma coerente e tecnicamente fundamentada, como seria o sistema responsável por:

- Organizar pousos de módulos da colônia  
- Gerenciar informações principais da operação  
- Estabelecer diretrizes de governança em uma colônia nascente em Marte  

---

## 1.1 Conteúdos Envolvidos

A atividade deverá ser desenvolvida com base exclusivamente nos conteúdos já trabalhados, articulando:

- Portas lógicas e funções booleanas  
- Estruturas avançadas de lógica e programação em Python  
- Estruturas lineares (listas, pilhas e filas)  
- Algoritmos clássicos de busca e ordenação  
- Modelagem de funções aplicadas  
- Histórico e evolução da computação  
- Princípios de governança ambiental, social e corporativa (ESG)  

---

## 1.2 Etapas da Atividade

### 1. Modelagem do cenário de pouso

- Definir um conjunto de módulos de pouso (ex: habitação, energia, laboratório, logística, suporte médico)  
- Descrever atributos básicos para cada módulo:
  - prioridade de pouso  
  - nível de combustível  
  - massa  
  - criticidade da carga  
  - horário estimado de chegada  

- Organizar os módulos em estruturas de dados lineares:
  - Fila (queue) principal de módulos aguardando pouso  
  - Listas auxiliares para módulos:
    - já pousados  
    - em espera  
    - em alerta  

---

### 2. Regras de decisão com portas lógicas

- Definir condições para autorizar ou bloquear o pouso, considerando:
  - combustível  
  - condições atmosféricas  
  - disponibilidade da área  
  - integridade dos sensores  

- Traduzir essas condições em:
  - expressões booleanas  
  - diagramas com portas lógicas (AND, OR, NOT)  

---

### 3. Implementação em Python

Desenvolver um script que:

- Cadastre os módulos em estruturas lineares  
- Implemente algoritmos de busca (ex: menor combustível, maior prioridade)  
- Aplique algoritmos de ordenação para reorganizar a fila  
- Simule decisões de pouso com base em lógica condicional (IF, ELIF, ELSE)  

**Observação:**  
O código deve ser simples, coerente com os conteúdos vistos e sem uso de bibliotecas avançadas.

---

### 4. Modelagem matemática

- Escolher um fenômeno relevante (ex: consumo de combustível, altura na descida, energia solar)  
- Representar por uma função matemática (linear, quadrática, exponencial, etc.)  
- Explicar:
  - fórmula  
  - parâmetros  
  - comportamento do gráfico  

- Relacionar com decisões do sistema (ex: momento de pouso, consumo crítico, etc.)

---

### 5. Contextualização histórica

- Relacionar o sistema com a evolução da computação  
- Abordar:
  - primeiros computadores  
  - sistemas embarcados  
  - limitações de hardware em Marte  

- Explicar como essas limitações influenciam:
  - algoritmos  
  - estruturas de dados  
  - estratégias de programação  

---

### 6. Princípios ESG

Elaborar uma reflexão considerando:

- Critérios para escolha da área de pouso  
- Gestão sustentável de recursos (energia, resíduos, etc.)  
- Mecanismos de governança e transparência  

---

## 2. ENTREGÁVEIS

Cada equipe deverá entregar:

### Relatório técnico (PDF – 5 a 10 páginas)

Deve conter:

- Descrição do cenário e módulos  
- Diagramas de portas lógicas  
- Modelagem matemática  
- Contextualização histórica  
- Reflexão ESG  

---

### Código fonte (.py)

- Protótipo do MGPEB  
- Organizado, comentado e executável  

---

### Anexo de estruturas de dados

- Descrição do uso de:
  - listas  
  - filas  
  - pilhas  

- Exemplos práticos no projeto  

---

## 3. Objetivo da Atividade

Esta atividade consolida o aprendizado ao colocar o aluno no papel de um engenheiro de sistemas, que precisa:

- Programar  
- Modelar  
- Organizar dados  
- Considerar limitações de hardware  
- Refletir sobre impactos sociais e ambientais  

O foco não é apenas técnico, mas também estratégico e responsável.