# Análise de Telemetria Pré-Decolagem — Aurora Siger

## Visão Geral
Análise de 1000 leituras de telemetria do sistema pré-decolagem da espaçonave Aurora Siger, validando parâmetros operacionais em relação aos requisitos de segurança.

## Organização do Repositório
O repositório contém:  

- **codes/**: Cada aluna desenvolveu seu próprio código Python.  
- **referencia/**: Contém os arquivos solicitados no trabalho, com exemplos e dados de referência.  
- **imagens/**: Todas as imagens utilizadas durante o projeto (gráficos, fluxogramas, diagramas).  
- **relatorio/**: Relatório final em PDF, consolidando códigos, análises e resultados.

## Conteúdo

### 1.0 — Imports e Configuração
- Configuração das bibliotecas: NumPy, Pandas, Seaborn, Matplotlib  
- Seed fixa (42) para reprodutibilidade  
- 1000 leituras simuladas (N=1000)  

### 1.1 — Dataset
Dados de telemetria simulados para:  
- Temperatura interna/externa  
- Integridade estrutural  
- Nível de energia  
- Pressão dos tanques  
- Módulos de navegação, comunicação e propulsão  

### 1.2 — Verificação
Classificação de status:  
- **PRONTO PARA DECOLAR**: Todos os sistemas e condições dentro das faixas seguras  
- **DECOLAGEM ABORTADA**: Um ou mais parâmetros fora da faixa segura  

### 1.3 — Tipos de Falha
Identificação e registro dos parâmetros que não atenderam aos critérios de segurança para cada leitura.  

### 1.4 — Visualização
Gráficos de barras mostrando:  
- Distribuição do status de prontidão para decolagem  
- Top 5 tipos de falha e suas frequências  

### 1.5 — Análise Energética
Cálculos de:  
- Capacidade de energia disponível (1500 kWh)  
- Nível de carga atual  
- Perdas do sistema (8%)  
- Consumo na decolagem (700 kWh)  
- Margem de energia e status de autonomia  

## Parâmetros de Segurança

| Parâmetro | Faixa Segura |
|-----------|--------------|
| Temperatura interna | 15 – 30 °C |
| Temperatura externa | -20 – 40 °C |
| Integridade estrutural | 1 |
| Nível de energia | ≥ 80% |
| Pressão dos tanques | 3 – 5 bar |
| Módulo de navegação | 1 |
| Módulo de comunicação | 1 |
| Módulo de propulsão | 1 |

## Requisitos
- numpy  
- pandas  
- seaborn  
- matplotlib  
