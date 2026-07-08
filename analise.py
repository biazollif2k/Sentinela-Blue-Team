def analisar_processos(processos):

    processos_interesse = [
        "powershell.exe",
        "cmd.exe",
        "python.exe",
        "wscript.exe",
        "cscript.exe"
    ]

    alertas = []

    for processo in processos:
        nome = processo["Nome"]

        if nome and nome.lower() in processos_interesse:
            alertas.append(processo)

    return alertas