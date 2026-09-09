bot_name: str = "RPA_FINANCEIRO_01"
max_retries: int = 3
execution_timeout: float = 30.0
is_production: bool = False

print(f"Nome do Bot: {bot_name} (Tipo: {type(bot_name)})")
print(f"Máximo de Tentativas: {max_retries} (Tipo: {type(max_retries)})")
print(f"Tempo limite de Execução: {execution_timeout} (Tipo: {type(execution_timeout)})")
print(f"Em Produção: {is_production} (Tipo: {type(is_production)})")
print("Robo pronto para rodar!")