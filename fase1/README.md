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

### Imports e Configuração
- Configuração das bibliotecas: NumPy, Pandas, Seaborn, Matplotlib  
- Seed fixa (42) para reprodutibilidade  
- 1000 leituras simuladas (N=1000)  

### Dataset
Dados de telemetria simulados para:  
- Temperatura interna/externa  
- Integridade estrutural  
- Nível de energia  
- Pressão dos tanques  
- Módulos de navegação, comunicação e propulsão  

### Verificação
Classificação de status:  
- **PRONTO PARA DECOLAR**: Todos os sistemas e condições dentro das faixas seguras  
- **DECOLAGEM ABORTADA**: Um ou mais parâmetros fora da faixa segura  

### Tipos de Falha
Identificação e registro dos parâmetros que não atenderam aos critérios de segurança para cada leitura.  

### Visualização
Gráficos de barras mostrando:  
- Distribuição do status de prontidão para decolagem  
- Top 5 tipos de falha e suas frequências  

### Análise Energética
Cálculos de:  
- Capacidade de energia disponível (1500 kWh)  
- Nível de carga atual  
- Perdas do sistema (8%)  
- Consumo na decolagem (700 kWh)  
- Margem de energia e status de autonomia  

## Análise Assistida por IA

Nesta etapa, utilizamos um modelo de regressão logística para classificar os dados de telemetria em relação ao risco de falha na decolagem, com base no status previamente definido ("PRONTO PARA DECOLAR" ou "DECOLAGEM ABORTADA").  

O modelo fornece uma probabilidade associada a cada leitura, indicando a chance de estar pronta para decolar, permitindo uma análise probabilística dos riscos.  

Além disso, geramos um gráfico clássico da regressão logística, que mostra a curva sigmoide típica do modelo, ilustrando visualmente a transição das probabilidades conforme o "score linear" calculado a partir dos dados processados.  

Essa abordagem facilita a identificação de leituras com maior risco, apoiando decisões técnicas mais precisas e baseadas em dados.  

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
