print("Meu projeto começou")
print("==============================")
print("       SENTINELA v1.5")
print("  Ferramenta de Segurança")
print("==============================")

print("\nSistema iniciado com sucesso!")

from sistema import coletar_informacoes, coletar_recursos
from processos import coletar_processos
from rede import coletar_conexoes
from relatorio import criar_relatorio
from logger import registrar_evento
from analise import analisar_processos

registrar_evento("Sistema iniciado")

print("==============================")
print("      SENTINELA BLUE TEAM")
print("==============================")

dados = coletar_informacoes()
processos = coletar_processos()
recursos = coletar_recursos()
conexoes = coletar_conexoes()
print("\nCONEXÕES DE REDE\n")

for conexao in conexoes[:10]:
    print(conexao)
alertas = analisar_processos(processos)

criar_relatorio(dados, processos, alertas, recursos)


registrar_evento("Relatório gerado com sucesso")
registrar_evento("Sistema encerrado")

print("\nAnálise concluída!")
print("Relatório criado com sucesso.")