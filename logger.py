import logging
import os

# Cria a pasta de logs caso não exista
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/sentinela.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)

def registrar_evento(mensagem):
    logging.info(mensagem)

def registrar_erro(mensagem):
    logging.error(mensagem)

def registrar_alerta(mensagem):
    logging.warning(mensagem)