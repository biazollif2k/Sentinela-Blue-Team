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

def coletar_processos():
    processos = []

    for processo in psutil.process_iter(['pid', 'name']):
        try:
            processos.append({
                "PID": processo.info['pid'],
                "Nome": processo.info['name']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return processos