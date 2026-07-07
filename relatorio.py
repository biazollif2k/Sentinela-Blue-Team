from datetime import datetime


def criar_relatorio(dados, processos):

    nome = "relatorio_seguranca.txt"

    with open(nome, "w", encoding="utf-8") as arquivo:
        arquivo.write("=" * 50 + "\n")
        arquivo.write("        RELATÓRIO SENTINELA BLUE TEAM\n")
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        arquivo.write("\n")

        arquivo.write("INFORMAÇÕES DO SISTEMA\n")
        arquivo.write("-" * 50 + "\n")

        for item, valor in dados.items():
            arquivo.write(f"{item:<22}: {valor}\n")

        arquivo.write("\n")
        arquivo.write("=" * 50 + "\n")
        arquivo.write("\n")

        arquivo.write("PROCESSOS EM EXECUÇÃO\n")
        arquivo.write("-" * 50 + "\n")

        for processo in processos:
            arquivo.write(
                f"PID: {processo['PID']:<8} Nome: {processo['Nome']}\n"
            )

        arquivo.write("\n")
        arquivo.write("=" * 50 + "\n")
        arquivo.write("Fim do relatório.\n")