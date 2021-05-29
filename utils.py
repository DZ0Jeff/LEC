import json
import random
from time import sleep
import pandas as pd


def get_contacts(type_job="CEO"):
    try:
        profiles = api.search_people(keyword_title=type_job)
        write_in_profile(profiles)
        print(f'Feito! {len(profiles)} contatos buscados')

    except Exception as error:
        print('Um erro aconteceu, tente novamente :(')
        raise
    

def write_in_profile(profiles):
    with open('profile.json','w') as file:
        json.dump(profiles, file)


def extract_names():
    names = []

    with open('profile.json','r') as file:
        profile_list = json.load(file)
        for data in profile_list:
            names.append(data['public_id'])

    return names


def extract_emails(target_name):
    extracted_emails = 0

    for list, name in enumerate(target_name):
        # GET a profiles contact info
        try:
            contact_info = api.get_profile_contact_info(name)
        
            if contact_info['email_address']:
                extracted_emails += 1
                print(f'Extraindo {extracted_emails} e-mail de contato')
                write_email(name, contact_info)      

        except Exception as error:
            print('Falha ao extrair! erro de conexão')
            pass

    print(f"{extracted_emails} e-mails extraidos, verifique 'email.json' para acesso ")  


def write_email(target_name, contact_info):
    with open('email.json','a') as file:
        json.dump(
        [
            {
                'name': target_name,
                "e-mail" : contact_info['email_address']
            },
        ], 
        file)


def save_to_json(data, filename):
    print('Salvando os dados em JSON')
    with open(f'{filename}.json','w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False)


def extract_link(link):
    try:
        print('> Limpando link')
        data = link.split('/')
        data = [x for x in data if x]
        print('> Usuário extraído')
        return data[-1]
    
    except Exception as error:
        print('> Link inválido, tente novamente')
        exit()


def JSONtoExcel(filename):
    try:
        print('Iniciando convensão...')
        df = pd.read_json(f'{filename}.json')
        df.to_excel(f'{filename}.xlsx')
        print('Convensão realizada com sucesso!')

    except Exception:
        print('Falha na conversão, Arquivo incorreto ou não existe...')


def check_param(param):
    try:
        param
    
    except KeyError:
        return "Não informado!"

    if param == None:
        return "Não existente"
    
    return param


def load_json(json_name):
    with open(f'{json_name}.json','r', encoding="utf-8") as file:
        data = json.load(file)

    return data
