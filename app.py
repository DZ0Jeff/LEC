from factory import getLinkedin
from utils import JSONtoExcel, save_to_json, extract_link, extract_json_data

links = [
    "https://www.linkedin.com/in/fabio-seiki-ishitani-240a3625/",
    "https://www.linkedin.com/in/rafaela-rompatto-corr%C3%AAa/"
]

profile_detail = []

def main():
    print('> Iniciando crawler..')
    api = getLinkedin()

    # for link in links
    user = extract_link("https://www.linkedin.com/in/fabio-seiki-ishitani-240a3625/")
    
    print('> Extraindo perfíl')
    profile = api.get_profile(user)

    data = extract_json_data(profile)

    print(data)

    print('Escrevendo no arquivo...')
    json_array = []
    json_array.append(data)
    save_to_json(json_array, 'data')
    print('Terminado!')
    JSONtoExcel('data')
    #  JSONJ

if __name__ == "__main__":
    main()