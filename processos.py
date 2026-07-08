import psutil


def coletar_processos():

    processos = []

    for processo in psutil.process_iter(["pid", "name"]):
        try:
            processos.append({
                "PID": processo.info["pid"],
                "Nome": processo.info["name"]
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return processos