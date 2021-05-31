from factory import getLinkedin
from utils import JSONtoExcel, remove_empty_elements, save_to_json, extract_link, remove_empty_elements, read_excel_file
from extractor import extract_json_data
from flatten_json import flatten
from random import randint
from time import sleep


# links = [
#     "https://www.linkedin.com/in/fabio-seiki-ishitani-240a3625/",
#     "https://www.linkedin.com/in/rafaela-rompatto-corr%C3%AAa/"
# ]

json_array = []
links = read_excel_file('crawler_linkedin_input.xlsx')

def main():
    print('[LPC]> Iniciando crawler..')
    api = getLinkedin()
    
    for link in links:
        print('[LPC]> Extraindo perfíl')
        user = extract_link(link)
        profile = api.get_profile(user)
        data = extract_json_data(profile)
        
        contact = api.get_profile_contact_info(user)
        flatten_contact = flatten(contact)
        data.update(flatten_contact)
        data = remove_empty_elements(data)

        print('[LPC]> Escrevendo no arquivo...')
        json_array.append(data)
        save_to_json(json_array, 'data')
        print('[LPC]> Terminado!')
        sleep(randint(10,100))

    JSONtoExcel('data')
    #  JSONJ

if __name__ == "__main__":
    main()