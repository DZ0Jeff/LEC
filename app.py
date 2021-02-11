from linkedin_api import Linkedin
import json

api = Linkedin('addtestfield@gmail.com','meuteste@01')


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


def write_email(target_name, contact_info):
    with open('email.json','a') as file:
        json.dump(
        {
            'name': target_name,
            "e-mail" : contact_info['email_address']
        }, 
        file)


def main():

    get_contacts(str(input('Digite a profissão desejada: ')))

    target_name = extract_names()

    for list, name in enumerate(target_name):
        
        print(f'Getting {list + 1} e-mail contact')
        # GET a profiles contact info
        contact_info = api.get_profile_contact_info(name)

        if contact_info != '':
            write_email(name, contact_info)      

    print(f"Feito! {len(target_name)} clintes extraidos, verifique 'email.json' para acesso ")  


if __name__ == "__main__":
    main()