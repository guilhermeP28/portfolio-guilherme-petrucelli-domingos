# 📊 Sistema de Auditoria de Orçamento Corporativo

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Visão Geral

Sistema avançado para cálculo e auditoria de orçamentos corporativos, desenvolvido em Python para demonstrar conceitos fundamentais de programação como **decorators**, **recursão**, **estruturas de dados aninhadas** e **parâmetros flexíveis**.

## 🎯 Conceitos Aplicados

| Conceito | Descrição |
|----------|------------|
| **Estrutura de Dados Aninhada** | Dicionário hierárquico simulando uma organização |
| **Recursão** | Navegação automática pela árvore de departamentos |
| ***args** | Permite ignorar departamentos dinamicamente |
| ****kwargs** | Configuração de moeda e taxa de câmbio |
| **Decorator @auditor** | Auditoria automática de tempo e parâmetros |

## 🏗️ Estrutura da Empresa

```python
estrutura_empresa = {
    "Matriz": {
        "TI": {
            "Infraestrutura": {"Servidores": 150k, "Redes": 80k, "Cloud": 200k},
            "Desenvolvimento": {"Backend": 320k, "Frontend": 280k, "QA": 90k},
            "Segurança": 110k
        },
        "RH": {"Recrutamento": 60k, "Treinamento": {...}, "Benefícios": 140k},
        "Financeiro": {"Contabilidade": 95k, "Controladoria": 75k, ...},
        "Marketing": {"Digital": {...}, "Branding": 70k, "Eventos": 90k}
    },
    "Filial SP": {"Operações": {...}, "Vendas": {...}},
    "Filial RJ": {"Operações": {...}, "Vendas": {...}, "P&D": {...}}
}
🚀 Funcionalidades
1. Auditoria Automática 📝
Registra timestamp de início

Lista departamentos ignorados

Mede tempo de execução (precisão em ms)

Formata saída com relatório detalhado

2. Cálculo Recursivo 🔄
Percorre automaticamente toda a hierarquia

Soma valores em qualquer nível de profundidade

Ignora subárvores inteiras quando necessário

3. Conversão de Moeda 💱
Suporte para múltiplas moedas (USD, EUR, etc.)

Taxa de câmbio configurável

Preserva total original em BRL

💻 Exemplos de Uso
Caso 1: Orçamento Total (BRL)
python
calcular_orcamento(estrutura_empresa)
Saída:

text
============================================================
          RELATÓRIO DE AUDITORIA FINANCEIRA
============================================================
  Função   : calcular_orcamento
  Início   : 2026-05-08 14:30:15
------------------------------------------------------------
  Departamentos ignorados : nenhum
  Parâmetros extras       : nenhum
------------------------------------------------------------
  Subtotal bruto (BRL)  : R$ 5,200,000.00
  Resultado final  : 5,200,000.00
  Tempo de execução: 0.2345 ms
============================================================
Caso 2: Ignorando Departamentos
python
calcular_orcamento(estrutura_empresa, "P&D", "Marketing")
💡 Ignora completamente os departamentos de Pesquisa & Desenvolvimento e Marketing

Caso 3: Conversão para USD
python
calcular_orcamento(
    estrutura_empresa,
    "Vendas",
    moeda_destino="USD",
    taxa_cambio=0.20
)
💡 Ignora Vendas e converte o total para Dólar Americano

Caso 4: Conversão para EUR
python
calcular_orcamento(
    estrutura_empresa,
    moeda_destino="EUR",
    taxa_cambio=0.18
)
📊 Exemplo de Relatório Completo
text
============================================================
          RELATÓRIO DE AUDITORIA FINANCEIRA
============================================================
  Função   : calcular_orcamento
  Início   : 2026-05-08 14:32:45
------------------------------------------------------------
  Departamentos ignorados : ('Vendas',)
  Parâmetros extras       : {'moeda_destino': 'USD', 'taxa_cambio': 0.20}
------------------------------------------------------------
  [IGNORADO] Departamento 'Vendas' excluído da auditoria.

  Subtotal bruto (BRL)  : R$ 3,950,000.00
  Taxa de câmbio        : 0.2 → USD
  Total convertido (USD): 790,000.00

  Resultado final  : 790,000.00
  Tempo de execução: 0.1892 ms
============================================================
🔧 Requisitos
Python 3.7 ou superior

Biblioteca time (nativa)

📦 Instalação
bash
# Clone o repositório
git clone https://github.com/seu-usuario/auditoria-corporativa.git

# Acesse o diretório
cd auditoria-corporativa

# Execute o sistema
python orcamento_empresa.py
🎓 Conceitos Técnicos Demonstrados
Decorator @auditor
python
def auditor(func):
    def wrapper(*args, **kwargs):
        # Medição de tempo
        # Log de parâmetros
        resultado = func(*args, **kwargs)
        # Relatório final
        return resultado
    return wrapper
Recursão para Navegação
python
def _somar(no, ignorados):
    for chave, valor in no.items():
        if chave in ignorados:
            continue
        if isinstance(valor, dict):
            total += _somar(valor, ignorados)
        else:
            total += valor
    return total
📈 Benefícios
✅ Transparência: Relatórios detalhados de cada execução

✅ Flexibilidade: Ignore departamentos sem modificar a estrutura

✅ Internacionalização: Conversão automática para múltiplas moedas

✅ Performance: Medição precisa de tempo de execução

✅ Manutenibilidade: Código limpo e bem documentado

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para:

Reportar bugs

Sugerir novas funcionalidades

Melhorar a documentação

Adicionar testes

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

📧 Contato
Autor: Guilherme Petrucelli Domingos

⭐ Desenvolvido para fins educacionais e demonstração de conceitos avançados de Python
