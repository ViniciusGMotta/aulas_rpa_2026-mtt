import logging

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("execucao_bot.log"),
        logging.StreamHandler()
    ]
)

def processar_arquivo(caminho: str):
    try:
        arquivo = open(caminho, "r")
        linhas = arquivo.readlines()
        for linha in linhas:
            logging.info(f"Linha lida: {linha.strip()}")
        arquivo.close()
    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado: {caminho}")
    finally:
        logging.info("Tentativa de processamento finalizada.")


# Exemplo de uso
processar_arquivo("dados.csv")