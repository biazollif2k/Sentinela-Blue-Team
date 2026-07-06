import platform


def coletar_informacoes():
    dados = {
        "Sistema operacional": platform.system(),
        "Versão": platform.version(),
        "Processador": platform.processor()
    }

    return dados