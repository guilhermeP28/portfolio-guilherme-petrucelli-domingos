# 🚚 LogisticsFlow & Inventory: Gestão Integrada de Pedidos e Estoque

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-blue)
![Python](https://img.shields.io/badge/linguagem-python-3.10-yellow)

## 📋 Sobre o Projeto
O **LogisticsFlow** evoluiu para um sistema integrado que gerencia não apenas o transporte, mas também o ciclo completo de venda e controle de estoque[cite: 9, 10]. A aplicação automatiza a verificação de disponibilidade, processamento de pagamentos e a atualização em tempo real do banco de dados de mercadorias[cite: 9, 11].

O projeto é dividido em módulos funcionais, garantindo que a lógica de negócio — desde a conferência de entrada até a emissão de comprovantes — seja executada de forma sequencial e segura[cite: 7, 10, 11].

## 🚀 Funcionalidades
*   **Gestão de Estoque:** Controle de entrada de mercadorias e atualização de saldos[cite: 9, 11].
*   **Verificação de Disponibilidade:** Bloqueio automático de vendas caso o saldo em estoque seja insuficiente[cite: 8, 9, 10].
*   **Processamento de Vendas:** Validação de transações financeiras para garantir que o valor pago cubra o valor da venda[cite: 7].
*   **Cálculo de Troco Automático:** Módulo que calcula a quantidade exata de cédulas (200, 50, 20, 10, 5, 2) para o troco do cliente[cite: 7].
*   **Logística de Distribuição:** Cálculo de rotas e monitoramento de veículos em trânsito[cite: 4, 6].
*   **Emissão de Comprovantes:** Geração de registros e notificações após a conclusão da venda e entrega[cite: 7, 10].

## 🧩 Arquitetura do Sistema
O sistema é estruturado em quatro módulos principais[cite: 7, 10]:

1.  **Módulo 1 (Entrada e Validação):** Recebimento de mercadorias e validação de transações financeiras[cite: 7, 11].
2.  **Módulo 2 (Processamento):** Adição de itens ao estoque, registro em banco de dados e cálculo de notas para troco[cite: 7, 9, 10].
3.  **Módulo 3 (Notificação):** Emissão de alertas de estoque insuficiente e cancelamento de processos quando necessário[cite: 8, 10].
4.  **Módulo 4 (Finalização):** Emissão de comprovantes de venda e conclusão do fluxo logístico[cite: 7, 10].

## 🛠️ Tecnologias Utilizadas
*   **Linguagem:** Python 3.10[cite: 7, 9].
*   **Estruturas de Dados:** Uso de Dicionários para controle de inventário (`estoque = {}`) e Listas para cédulas de troco[cite: 7, 9].
*   **Lógica de Programação:** Operadores de divisão inteira (`//`) e módulo (`%`) para cálculo de cédulas, além de funções modulares para cada etapa do processo[cite: 7, 9].

## ⚙️ Como Executar
1. Clone o repositório:
   
```bash
   git clone [https://github.com/seu-usuario/logistics-flow.git](https://github.com/seu-usuario/logistics-flow.git)
