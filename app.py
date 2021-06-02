from factory import getLinkedin
from utils import JSONtoExcel, remove_empty_elements, save_to_json, extract_link, remove_empty_elements, read_excel_file, save_counter
from extractor import extract_json_data
from flatten_json import flatten


json_array = []


def main():
    print('[LPC]> Iniciando crawler..')
    api = getLinkedin()
    links = read_excel_file('crawler_linkedin_input.xlsx')
    
    for index, link in enumerate(links):
        print(f'{index} usuário')
        save_counter(index)
        if index >= 153:
            print('[LPC]> Extraindo perfíl')
            user = extract_link(link)
            print(user)
            
            try:
                profile = api.get_profile(user)
            
            except KeyError:
                print('Usúario inválido')
                continue

            except Exception as error:
                print(f'> [ERRO] {error}')
                print('Usúario inválido')
                exit()

            data = extract_json_data(profile)
            
            contact = api.get_profile_contact_info(user)
            flatten_contact = flatten(contact)
            data.update(flatten_contact)
            data = remove_empty_elements(data)

            print('[LPC]> Escrevendo no arquivo...')
            json_array.append(data)
            save_to_json(json_array, 'data')
            print('[LPC]> Terminado!')
            

            if index != 0 and index % 50 == 0:
                print('Limite atingido! Tentge novamente amanhã')
                exit() 

    JSONtoExcel('data')
    #  JSONJ

if __name__ == "__main__":
    main()