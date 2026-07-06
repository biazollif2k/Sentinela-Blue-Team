from datetime import datetime


def criar_relatorio(dados):

    nome = "relatorio_seguranca.txt"

    with open(nome, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO SENTINELA BLUE TEAM\n")
        arquivo.write("============================\n")
        arquivo.write(f"Data: {datetime.now()}\n\n")

        for item, valor in dados.items():
            arquivo.write(f"{item}: {valor}\n")