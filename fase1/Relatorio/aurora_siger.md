# AURORA SIGER
### Relatório Operacional de Pré-Decolagem

---

**Arthur Oliveira · Bryan Lima Garcia · Dayvid Daniel · Matheus Resende · Vinicius Valiati**

*Ciência da Computação — FIAP*

---

## Introdução

Este relatório apresenta a análise operacional de pré-decolagem da nave **Aurora Siger**, com o objetivo de verificar se todas as condições necessárias para o lançamento estão dentro dos padrões de segurança estabelecidos. A validação foi realizada a partir da interpretação dos dados de telemetria, incluindo temperatura, integridade estrutural, níveis de energia, pressão dos tanques e funcionamento dos módulos críticos.

Com base nesses dados, desenvolvemos um algoritmo de verificação utilizando lógica, capaz de decidir automaticamente entre **"PRONTO PARA DECOLAR"** ou **"DECOLAGEM ABORTADA"**. Essa lógica foi implementada em Python, simulando o funcionamento de rotinas utilizadas em sistemas embarcados.

Além disso, foi realizada uma análise energética para calcular a autonomia inicial da nave, considerando capacidade total, carga atual, consumo estimado e perdas energéticas. Também foi utilizada uma abordagem assistida por inteligência artificial para classificar os dados e identificar possíveis riscos.

O relatório integra análise técnica, programação e reflexão crítica, demonstrando como diferentes áreas do conhecimento podem ser aplicadas na validação de uma missão espacial.

---

## Telemetria

Todos os parâmetros analisados devem estar dentro das faixas seguras estabelecidas abaixo. Sendo assim, a fase inicial da missão pode ser iniciada, com a integridade estrutural preservada, os módulos críticos estando operacionais e os níveis de energia sendo suficientes.

| Parâmetro | Faixa Segura |
|---|---|
| Temperatura interna | 15 – 30 °C |
| Temperatura externa | -20 – 40 °C |
| Integridade estrutural | 1 |
| Nível de energia | ≥ 80% |
| Pressão dos tanques | 3 – 5 bar |
| Módulo de Navegação | 1 |
| Módulo de Comunicação | 1 |
| Módulo de Propulsão | 1 |

---

## Algoritmo de Verificação

### Pseudocódigo

```
SE integridade estrutural = 0   → DECOLAGEM ABORTADA
SE energia < 80%                → DECOLAGEM ABORTADA
SE pressão < 3 OU > 5           → DECOLAGEM ABORTADA
SE qualquer módulo crítico = 0  → DECOLAGEM ABORTADA
CASO CONTRÁRIO                  → PRONTO PARA DECOLAR
```

---

## Análise Energética

### Dados utilizados

- **Capacidade total:** 1500 kWh
- **Consumo estimado na decolagem:** 700 kWh
- **Perdas energéticas:** 8%

### Cálculos

A energia disponível é obtida multiplicando a capacidade total pelo percentual de carga atual indicado na telemetria:

```
Energia disponível = Capacidade total × (Percentual de carga / 100)
```

Cálculo das perdas energéticas:

```
Perdas = Energia disponível × 0,08
```

Cálculo da energia real utilizável:

```
Energia real = Energia disponível − Perdas
```

Após determinar a energia real disponível, o valor é comparado com o consumo estimado para a decolagem (700 kWh).

### Conclusão Energética

Caso a **energia real seja maior ou igual ao consumo necessário**, a nave possui autonomia suficiente para a decolagem. Caso contrário, a missão deve ser abortada por insuficiência energética.

---

## Análise Assistida por IA

A inteligência artificial pode ser utilizada como ferramenta auxiliar para classificar os dados operacionais e identificar possíveis riscos.

**Critérios analisados:**

- Nível de energia próximo do limite mínimo
- Pressão fora da faixa ideal
- Inconsistência entre módulos críticos

Com base nos dados fornecidos, a classificação de risco foi considerada **baixa**, não sendo identificadas anomalias significativas que comprometam o lançamento.

---

## Reflexão Crítica

A exploração espacial exige responsabilidade técnica e ética. Um lançamento envolve riscos que podem impactar vidas humanas, o meio ambiente e recursos financeiros significativos. Por isso, **decisões automatizadas devem sempre priorizar segurança** acima de cronogramas ou metas.

Além disso, o avanço científico deve caminhar junto com a responsabilidade social e ambiental — é fundamental considerar a sustentabilidade tecnológica, reduzindo desperdícios energéticos e minimizando a geração de detritos espaciais.

---

## Conclusão Final

Após a análise completa da telemetria, da verificação algorítmica, da implementação em Python e da avaliação energética, podemos concluir se a nave **Aurora Siger** apresenta condições operacionais adequadas para o lançamento ou não.