from factory import getLinkedin
from utils import JSONtoExcel, save_to_json, extract_link
from extractor import extract_json_data
import json

links = [
    "https://www.linkedin.com/in/fabio-seiki-ishitani-240a3625/",
    "https://www.linkedin.com/in/rafaela-rompatto-corr%C3%AAa/"
]

json_array = []

def main():
    print('[LPC]> Iniciando crawler..')
    api = getLinkedin()
    
    for link in links:
        print('[LPC]> Extraindo perfíl')
        user = extract_link(link)
        profile = api.get_profile(user)
        data = extract_json_data(profile)
        
        contact = api.get_profile_contact_info(user)
        data.update(contact)

        print('[LPC]> Escrevendo no arquivo...')
        json_array.append(data)
        save_to_json(json_array, 'data')
        print('[LPC]> Terminado!')

    JSONtoExcel('data')
    #  JSONJ

if __name__ == "__main__":
    main()