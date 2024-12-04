import os
from dotenv import load_dotenv
from modules.logger import get_logger

# Função de logging
logger = get_logger()

def check_env_var(var_name):
    """
    Função para verificar se uma variável de ambiente existe e não está vazia.

    :param var_name: Nome da variável de ambiente
    """
    value = os.getenv(var_name)
    
    if not value or not value.strip():
        erro = f"A variável de ambiente {var_name} não foi encontrada no arquivo .env!"
        logger.error(erro)
        raise ValueError(erro)
    return value
         
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica as variáveis de ambiente do email do Zimbra
ZIMBRA_EMAIL = check_env_var("ZIMBRA_EMAIL")
ZIMBRA_EMAIL_PASSWORD = check_env_var("ZIMBRA_EMAIL_PASSWORD")
SMTP_SERVER = check_env_var("SMTP_SERVER")
SMTP_PORT = check_env_var("SMTP_PORT")

# Verifica as variáveis de ambiente de conexão com banco de dados
DB_NAME = check_env_var("DB_NAME")
DB_USER = check_env_var("DB_USER")
DB_PASSWORD = check_env_var("DB_PASSWORD")