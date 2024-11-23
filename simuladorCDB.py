def simular_cdb(valor_inicial, taxa_cdi, cdi_atual, meses):
    """
    Simula o rendimento de um CDB com base nos parâmetros fornecidos.
    :param valor_inicial: Valor inicial investido (float).
    :param taxa_cdi: Taxa de rentabilidade (% do CDI, float).
    :param cdi_atual: CDI anual (em %, float).
    :param meses: Período do investimento (em meses, int).
    :return: Dicionário com valor inicial, valor final e lucro.
    """
    cdi_mensal = (1 + cdi_atual / 100) ** (1 / 12) - 1  # CDI mensal
    taxa_mensal = cdi_mensal * (taxa_cdi / 100)  # Rentabilidade mensal baseada no CDI

    valor_final = valor_inicial

    for _ in range(meses):
        valor_final *= (1 + taxa_mensal)

    return {
        "valor_inicial": round(valor_inicial, 2),
        "valor_final": round(valor_final, 2),
        "lucro": round(valor_final - valor_inicial, 2),
    }

# Captura de entrada do usuário
def obter_input_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")

def obter_input_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Programa principal
def main():
    print("Simulador de CDB")
    
    valor_inicial = obter_input_float("Digite o valor inicial do investimento (R$): ")
    taxa_cdi = obter_input_float("Digite a taxa de rentabilidade (% do CDI): ")
    cdi_atual = obter_input_float("Digite o CDI atual (anual em %): ")
    meses = obter_input_int("Digite o período do investimento (em meses): ")

    resultado = simular_cdb(valor_inicial, taxa_cdi, cdi_atual, meses)

    print("\nResultado da Simulação:")
    print(f"Valor Inicial: R$ {resultado['valor_inicial']}")
    print(f"Valor Final: R$ {resultado['valor_final']}")
    print(f"Lucro: R$ {resultado['lucro']}")

if __name__ == "__main__":
    main()
