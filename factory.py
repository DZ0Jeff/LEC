from linkedin_api import Linkedin
from dotenv import load_dotenv
import os

load_dotenv()


def getLinkedin(login, password):
    # iniciar uma instância do linkedin
    # login = os.environ.get('LINKEDIN_USER')
    # password = os.environ.get('LINKEDIN_PASSWORD')

    try:
        print(login)
        print(password)

        api = Linkedin(login, password, refresh_cookies=True)
        return api
    
    except Exception as error:
        raise
        print('> [LPC] Algo deu errado no login...')
        print(f'> [LPC] [ERRO] {error}')
        exit()