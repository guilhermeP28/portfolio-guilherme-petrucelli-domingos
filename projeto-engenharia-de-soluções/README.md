# 🚚 LogisticsFlow: Inteligência e Automação de Pedidos

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-blue)
![Python](https://img.shields.io/badge/linguagem-python-3.10-yellow)

## 📋 Sobre o Projeto
O **LogisticsFlow** é um sistema desenvolvido em Python focado na automação e otimização do ciclo de vida de pedidos logísticos[cite: 4, 6]. O projeto integra uma lógica de decisão robusta para gerenciar desde a entrada de dados e verificação de estoque até o monitoramento em trânsito e fluxos de contingência para reentrega[cite: 5, 6].

Este sistema foi modelado com base em fluxogramas técnicos, garantindo que cada etapa da operação siga regras de negócio precisas para mitigar falhas de entrega e atrasos operacionais[cite: 6].

## 🚀 Funcionalidades
*   **Entrada de Pedidos:** Registro centralizado de solicitações de clientes e entrada de dados[cite: 4, 6].
*   **Gestão de Estoque Inteligente:** Verificação automática de disponibilidade; o sistema entra em modo de espera por reposição caso o item não esteja disponível[cite: 4, 6].
*   **Cálculo de Rota e Logística:** Motor que processa a distância para calcular rotas de transporte eficientes[cite: 4].
*   **Monitoramento em Tempo Real:** Simulação de rastreio de veículos com status "Em Trânsito"[cite: 4, 6].
*   **Fluxo de Reentrega (Contingência):** Lógica dedicada para tratar entregas não realizadas, permitindo o reinício do ciclo de trânsito[cite: 5].

## 🧩 Fluxo de Processamento
O sistema segue rigorosamente o modelo lógico abaixo[cite: 6]:

1.  **Início do Pedido:** Captura da solicitação[cite: 4].
2.  **Validação de Estoque:** Decisão crítica para prosseguimento ou retenção para reposição[cite: 4, 6].
3.  **Preparação Logística:** Validação do pedido e preparação do veículo[cite: 4].
4.  **Trânsito:** Cálculo de rota e monitoramento ativo[cite: 4, 6].
5.  **Verificação de Entrega:** Decisão baseada no sucesso do recebimento[cite: 5, 6].
    *   **Sucesso:** Finalização da entrega[cite: 1, 3].
    *   **Falha:** Acionamento do centro de decisão para reentrega ou encerramento com problemas[cite: 5].

## 🛠️ Tecnologias Utilizadas
*   **Linguagem:** Python 3.10[cite: 4, 5].
*   **Conceitos de Programação:** Estruturas condicionais avançadas (`if/else`), sanitização de dados (`.lower()`), conversão de tipos e funções modulares[cite: 4, 5].
*   **Modelagem de Sistemas:** Fluxogramas de processos de transporte[cite: 6].

## ⚙️ Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/logistics-flow.git](https://github.com/seu-usuario/logistics-flow.git)
