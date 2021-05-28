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
    with open(f'{filename}.json','w', encoding='utf-8') as file:
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


# Extract JSON
def extract_json_data(profile):
    data = dict()
    data['Sumário'] = profile["summary"]
    data['Name'] = profile['firstName'] + ' ' + profile['lastName']
    data['Ocupação'] = profile["headline"]
    data['Localização'] = profile["geoLocationName"] + ' ' + profile['locationName']
    
    # Experiência
    conpany_detail = get_experience(profile)
    data['Empresas'] = '*'.join(conpany_detail)

    # Graduação
    education = get_education()
    data['Educação'] = '*'.join(education)
    
    # certificados 
    
    certificates = get_certificates()
    data['Certificados'] = '*'.join(certificates)

    return data


def get_experience(profile):
    company_detail = []
    for experience in profile["experience"]:
       
        location = check_param(experience.get("locationName"))
        name_of_company = check_param(experience.get('companyName'))
        conpany_description = check_param(experience.get("description"))

        startTime = ''
        try:
            startTime = check_param(experience['timePeriod']['startDate']['year'])
        
        except KeyError:
            startTime = 'Não existente'

        endTime = ''
        try:
            endTime = check_param(experience['timePeriod']['endDate']['year'])
        
        except KeyError:
            try:
                endTime = check_param(experience['timePeriod']['startDate']['year'])
            
            except Exception:
                endTime = 'Não existente'

        interval = f"{startTime}/{endTime}"

        level = check_param(experience.get("title"))

        experience_result = f"\nNome: {name_of_company} \nLocalização: {location} \nDescrição: {conpany_description} \nTempo de trabalho: {interval} \nNível: {level} \n\n*"
        company_detail.append(experience_result)

    return company_detail


def get_education(profile):
    education = []
    for study in profile["education"]:
        school_name = check_param(study.get("schoolName"))
        degree = check_param(study.get("degreeName"))

        startTime = ''
        try:
            startTime = check_param(study['timePeriod']['startDate']['year'])
        
        except KeyError:
            startTime = 'Não existente'

        endTime = ''
        try:
            endTime = check_param(study['timePeriod']['endDate']['year'])
        
        except KeyError:
            try:
                endTime = check_param(study['timePeriod']['startDate']['year'])
            
            except Exception:
                endTime = 'Não existente'

        duration = f"De {startTime}/{endTime}"
        field = check_param(study.get("fieldOfStudy"))

        education_field = f"\nNome da instítuição: {school_name} \nNível: {degree} \nDuração: {duration} \nÁrea: {field}\n*"
        education.append(education_field)
    
    return education


def get_certificates(profile):
    certificates = []
    for certificate in profile["certifications"]:
        autority = certificate.get("authority")
        name = certificate.get("name")

        # get interval
        startTime = ''
        try:
            startTime = check_param(certificate['timePeriod']['startDate']['year'])
        
        except KeyError:
            startTime = 'Não existente'

        endTime = ''
        try:
            endTime = check_param(certificate['timePeriod']['endDate']['year'])
        
        except KeyError:
            try:
                endTime = check_param(certificate['timePeriod']['startDate']['year'])
            
            except Exception:
                endTime = 'Não existente'

        interval = f"{startTime}/{endTime}"
        url = check_param(certificate.get('url'))
        
        certificates_info = f"\nAutoridade: {autority}\nNome: {name} \nIntervalo: {interval}\n{url}*"
        print(certificates_info)
        certificates.append(certificates_info)

    return certificates
