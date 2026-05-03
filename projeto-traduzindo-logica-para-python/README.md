# 🚚 LogisticsFlow & Inventory: Gestão Integrada de Pedidos e Estoque

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-blue)
![Python](https://img.shields.io/badge/linguagem-python-3.10-yellow)

## 📋 Sobre o Projeto
O **LogisticsFlow** é um sistema completo para automação do ciclo comercial e logístico[cite: 4, 9]. Ele integra o gerenciamento de estoque, o processamento de vendas com cálculo de troco e a roteirização de entregas[cite: 7, 10, 11].

O projeto foi construído focando na correta tipagem de dados e no controle de fluxo, garantindo que as operações matemáticas (como soma de estoque e cálculo de troco) ocorram sem erros de execução[cite: 7, 12].

## 🚀 Funcionalidades
*   **Gestão de Inventário:** Controle de entrada de mercadorias e atualização de saldos em tempo real[cite: 9, 11].
*   **Processamento de Vendas:** Validação de transações financeiras e verificação de disponibilidade de estoque antes da confirmação[cite: 7, 8, 10].
*   **Cálculo Automático de Troco:** Módulo que identifica a quantidade exata de cada cédula (de R$ 2 a R$ 200) para o cliente[cite: 7].
*   **Logística e Distribuição:** Cálculo de rotas baseadas em distância e monitoramento do status "Em Trânsito"[cite: 4, 6].
*   **Tratamento de Contingências:** Fluxo para reentrega em caso de falha no recebimento[cite: 5, 10].

## 🧩 Arquitetura do Sistema
O sistema é organizado de forma modular para facilitar a manutenção[cite: 7, 10]:

1.  **Módulo de Entrada (Validação):** Recebe mercadorias e valida se o valor pago cobre o custo da venda[cite: 7, 11].
2.  **Módulo de Processamento (Cálculo):** Registra dados no estoque e utiliza lógica matemática para calcular o troco[cite: 7, 9].
3.  **Módulo Logístico (Transporte):** Define rotas e acompanha o veículo até a entrega final[cite: 4, 6].
4.  **Módulo de Notificação:** Emissão de comprovantes ou alertas de "Estoque Insuficiente"[cite: 8, 10].

## 🛠️ Detalhes Técnicos de Implementação
Para garantir a robustez do software, foram aplicadas as seguintes práticas de Python[cite: 12]:
*   **Tipagem de Dados:** Uso obrigatório de `int()` e `float()` nas funções de `input()`, prevenindo erros de concatenação de strings em cálculos financeiros[cite: 12].
*   **Controle de Laços:** Uso estratégico da função `range(início, fim + 1)` para garantir que todos os períodos (como meses ou itens) sejam processados corretamente, respeitando o comportamento exclusivo do limite superior em Python[cite: 12].
*   **Estruturas de Dados:** Uso de dicionários para mapeamento de estoque e listas para cédulas monetárias[cite: 7, 9].

## ⚙️ Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/logistics-flow.git](https://github.com/seu-usuario/logistics-flow.git)
