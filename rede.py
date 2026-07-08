import psutil


def coletar_conexoes():

    conexoes = []

    for conexao in psutil.net_connections(kind="inet"):
        try:
            conexoes.append({
                "Protocolo": "TCP" if conexao.type == 1 else "UDP",
                "IP Local": conexao.laddr.ip if conexao.laddr else "",
                "Porta Local": conexao.laddr.port if conexao.laddr else "",
                "IP Remoto": conexao.raddr.ip if conexao.raddr else "",
                "Porta Remota": conexao.raddr.port if conexao.raddr else "",
                "Status": conexao.status
            })
        except (AttributeError, PermissionError):
            pass

    return conexoes