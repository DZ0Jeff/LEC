from json.decoder import JSONDecodeError
from factory import getLinkedin
from utils import JSONtoExcel, RotateAccounts, extract_profiles_from_company, remove_empty_elements, save_to_json, extract_link, remove_empty_elements, read_excel_file, save_counter, generate_random_time
from extractor import extract_json_data
from flatten_json import flatten
from account import accounts
import os

json_array = []


def main():
    print('[LPC]> Iniciando crawler..')
    account = RotateAccounts(accounts)
    next_account = account.nextAccount()

    print(next_account)

    links = read_excel_file('data/Zé Delivery.xlsx')
    api = getLinkedin(next_account["user"], next_account["password"])
    
    for index, link in enumerate(links):
        print(f'{index} usuário')
        if index >= 206:
            save_counter(index)
            
            print('[LPC]> Extraindo perfíl')
            user = extract_link(link)
            print(user)
            
            try:
                profile = api.get_profile(user)
            
            except KeyError:
                print('Usúario inválido')
                continue

            except ValueError:
                print('Erro da conta, verificar e tente novamente!')
                exit()

            except Exception as error:
                print(f'> [ERRO] {error}')
                continue

            try:
                data = extract_json_data(profile, link)
            except KeyError:
                print('> Não existem dados....')
                continue
            
            generate_random_time()
            try:
                contact = api.get_profile_contact_info(user)
            
            except JSONDecodeError:
                print('>[LPC]> informações inválidas!')

            flatten_contact = flatten(contact)
            data.update(flatten_contact)
            data = remove_empty_elements(data)

            print('[LPC]> Escrevendo no arquivo...')
            json_array.append(data)
            save_to_json(json_array, 'data')
            print('[LPC]> Terminado!')
            generate_random_time()

            if index != 0 and index % 50 == 0:
                print('Limite atingido! Trocando de conta...')
                next_account = account.nextAccount()
                api = getLinkedin(next_account["user"], next_account["password"])

    # extract_profiles_from_company('Zé Delivery')
    # JSONtoExcel('Zé Delivery')
    # profiles = read_excel_file('Zé Delivery.xlsx')
    # print(len(profiles))

if __name__ == "__main__":
    main()
