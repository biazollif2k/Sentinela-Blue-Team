print("Meu projeto começou")
print("==============================")
print("       SENTINELA v1.0")
print("  Ferramenta de Segurança")
print("==============================")

print("\nSistema iniciado com sucesso!")

from sistema import coletar_informacoes, coletar_processos
from relatorio import criar_relatorio
from logger import registrar_evento

registrar_evento("Sistema iniciado")

print("==============================")
print("      SENTINELA BLUE TEAM")
print("==============================")

dados = coletar_informacoes()
processos = coletar_processos()

criar_relatorio(dados, processos)


registrar_evento("Relatório gerado com sucesso")
registrar_evento("Sistema encerrado")

print("\nAnálise concluída!")
print("Relatório criado com sucesso.")