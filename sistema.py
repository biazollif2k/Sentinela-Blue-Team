import platform
import getpass
import psutil
from datetime import datetime


def coletar_informacoes():
    dados = {
        "Sistema operacional": platform.system(),
        "Versão": platform.version(),
        "Processador": platform.processor(),
        "Nome do computador": platform.node(),
        "Usuário": getpass.getuser(),
        "Versão do Python": platform.python_version(),
        "Data e hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    return dados





def coletar_recursos():

    recursos = {
        "CPU (%)": psutil.cpu_percent(interval=1),
        "Memória (%)": psutil.virtual_memory().percent,
        "Disco (%)": psutil.disk_usage("/").percent
    }

    return recursos