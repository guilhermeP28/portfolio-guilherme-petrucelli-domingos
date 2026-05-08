"""
orcamento_empresa.py
====================
Sistema de cálculo de orçamento corporativo com auditoria.

Conceitos aplicados:
    - Estrutura de dados aninhada (dicionário/árvore)
    - Recursão
    - *args  (departamentos a ignorar)
    - **kwargs (conversão de moeda: moeda_destino, taxa_cambio)
    - Decorator @auditor (tempo de execução + log de auditoria)
"""

import time


# ---------------------------------------------------------------------------
# 1. DECORATOR @auditor
# ---------------------------------------------------------------------------

def auditor(func):
    """
    Decorator de auditoria financeira.

    Intercepta qualquer chamada da função decorada e:
        - Exibe cabeçalho com nome da função e timestamp de início;
        - Registra os argumentos recebidos (*args e **kwargs);
        - Mede e exibe o tempo total de execução;
        - Exibe o resultado retornado pela função.
    """

    def wrapper(*args, **kwargs):
        # ── Cabeçalho ──────────────────────────────────────────────────────
        print("=" * 60)
        print("          RELATÓRIO DE AUDITORIA FINANCEIRA")
        print("=" * 60)
        print(f"  Função   : {func.__name__}")
        print(f"  Início   : {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 60)

        # ── Registro dos argumentos ────────────────────────────────────────
        # args[0] é o dicionário de estrutura; os demais são os departs. ignorados
        departamentos_ignorados = args[1:] if len(args) > 1 else ()
        print(f"  Departamentos ignorados : {departamentos_ignorados if departamentos_ignorados else 'nenhum'}")
        print(f"  Parâmetros extras       : {kwargs if kwargs else 'nenhum'}")
        print("-" * 60)

        # ── Execução + medição de tempo ────────────────────────────────────
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()

        tempo_ms = (fim - inicio) * 1_000  # converte para milissegundos

        # ── Rodapé ─────────────────────────────────────────────────────────
        print(f"  Resultado final  : {resultado:,.2f}")
        print(f"  Tempo de execução: {tempo_ms:.4f} ms")
        print("=" * 60)

        return resultado

    return wrapper


# ---------------------------------------------------------------------------
# 2. ESTRUTURA DE DADOS — Dicionário aninhado simulando a empresa
# ---------------------------------------------------------------------------

estrutura_empresa = {
    "Matriz": {
        "TI": {
            "Infraestrutura": {
                "Servidores": 150_000.00,
                "Redes": 80_000.00,
                "Cloud": 200_000.00,
            },
            "Desenvolvimento": {
                "Backend": 320_000.00,
                "Frontend": 280_000.00,
                "QA": 90_000.00,
            },
            "Segurança": 110_000.00,
        },
        "RH": {
            "Recrutamento": 60_000.00,
            "Treinamento": {
                "Cursos Internos": 30_000.00,
                "Certificações": 25_000.00,
            },
            "Benefícios": 140_000.00,
        },
        "Financeiro": {
            "Contabilidade": 95_000.00,
            "Controladoria": 75_000.00,
            "Auditoria Interna": 50_000.00,
        },
        "Marketing": {
            "Digital": {
                "SEO": 40_000.00,
                "Mídia Paga": 180_000.00,
                "Redes Sociais": 35_000.00,
            },
            "Branding": 70_000.00,
            "Eventos": 90_000.00,
        },
    },
    "Filial SP": {
        "Operações": {
            "Logística": 210_000.00,
            "Estoque": 85_000.00,
        },
        "Vendas": {
            "Varejo": 300_000.00,
            "Corporativo": 450_000.00,
            "Suporte ao Cliente": 60_000.00,
        },
    },
    "Filial RJ": {
        "Operações": {
            "Logística": 175_000.00,
            "Estoque": 65_000.00,
        },
        "Vendas": {
            "Varejo": 220_000.00,
            "Corporativo": 310_000.00,
        },
        "P&D": {
            "Pesquisa": 500_000.00,
            "Inovação": 350_000.00,
        },
    },
}


# ---------------------------------------------------------------------------
# 3. FUNÇÃO PRINCIPAL — calcular_orcamento
# ---------------------------------------------------------------------------

@auditor
def calcular_orcamento(estrutura, *args, **kwargs):
    """
    Calcula recursivamente o orçamento total de uma estrutura hierárquica.

    Parâmetros
    ----------
    estrutura : dict
        Dicionário (possivelmente aninhado) com os orçamentos.
    *args : str
        Nomes de departamentos/nós a serem completamente ignorados
        (o nó e toda a sua subárvore são excluídos da soma).
    **kwargs :
        moeda_destino (str)  — nome/sigla da moeda de saída (ex.: "USD").
        taxa_cambio   (float)— fator de conversão aplicado ao total (ex.: 0.20).

    Retorno
    -------
    float
        Soma dos valores folha, ajustada pela taxa de câmbio (se fornecida).
    """

    def _somar(no, ignorados):
        """
        Função auxiliar recursiva que percorre a árvore e acumula valores.

        Para cada elemento do dicionário:
            - Se a chave estiver na lista de ignorados → pula o nó inteiro.
            - Se o valor for um dicionário → desce recursivamente.
            - Se o valor for numérico (int/float) → adiciona à soma.
        """
        total = 0.0

        for chave, valor in no.items():
            # Ignora departamentos listados em *args
            if chave in ignorados:
                print(f"  [IGNORADO] Departamento '{chave}' excluído da auditoria.")
                continue

            if isinstance(valor, dict):
                # Nó interno: desce um nível
                total += _somar(valor, ignorados)
            elif isinstance(valor, (int, float)):
                # Nó folha: soma o valor orçamentário
                total += valor

        return total

    # Converte args para conjunto para busca O(1)
    departamentos_ignorados = set(args)

    # Calcula o total bruto (moeda original)
    total_bruto = _somar(estrutura, departamentos_ignorados)

    # Aplica conversão de moeda se os kwargs correspondentes forem fornecidos
    taxa = kwargs.get("taxa_cambio", 1.0)
    moeda = kwargs.get("moeda_destino", "BRL")

    total_convertido = total_bruto * taxa

    print(f"\n  Subtotal bruto (BRL)  : R$ {total_bruto:,.2f}")
    if taxa != 1.0:
        print(f"  Taxa de câmbio        : {taxa} → {moeda}")
        print(f"  Total convertido ({moeda}): {total_convertido:,.2f}\n")

    return total_convertido


# ---------------------------------------------------------------------------
# 4. DEMONSTRAÇÕES DE USO
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("\n\n>>> CASO 1: Orçamento total sem exclusões, em BRL\n")
    calcular_orcamento(estrutura_empresa)

    print("\n\n>>> CASO 2: Ignorando 'P&D' e 'Marketing', em BRL\n")
    calcular_orcamento(estrutura_empresa, "P&D", "Marketing")

    print("\n\n>>> CASO 3: Ignorando 'Vendas', convertendo para USD\n")
    calcular_orcamento(
        estrutura_empresa,
        "Vendas",
        moeda_destino="USD",
        taxa_cambio=0.20,
    )

    print("\n\n>>> CASO 4: Sem exclusões, convertendo para EUR\n")
    calcular_orcamento(
        estrutura_empresa,
        moeda_destino="EUR",
        taxa_cambio=0.18,
    )
