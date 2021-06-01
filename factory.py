from linkedin_api import Linkedin
from dotenv import load_dotenv
import os

load_dotenv()


def getLinkedin():
    # iniciar uma instância do linkedin
    login = os.environ.get('LINKEDIN_USER')
    password = os.environ.get('LINKEDIN_PASSWORD')

    try:
        api = Linkedin(login, password)
        return api
    
    except Exception as error:
        print('> [LPC] Algo deu errado no login...')
        print(f'> [LPC] [ERRO] {error}')