print("Meu projeto começou")
print("==============================")
print("       SENTINELA v1.0")
print("  Ferramenta de Segurança")
print("==============================")

print("\nSistema iniciado com sucesso!")
from sistema import coletar_informacoes
from relatorio import criar_relatorio

print("==============================")
print("      SENTINELA BLUE TEAM")
print("==============================")

dados = coletar_informacoes()

criar_relatorio(dados)

print("\nAnálise concluída!")
print("Relatório criado com sucesso.")