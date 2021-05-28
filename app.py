from factory import getLinkedin
from utils import JSONtoExcel, save_to_json, extract_link

links = [
    "https://www.linkedin.com/in/fabio-seiki-ishitani-240a3625/",
    "https://www.linkedin.com/in/rafaela-rompatto-corr%C3%AAa/"
]

def main():
    print('> Iniciando crawler..')
    api = getLinkedin()

    # for link in links:
    data = dict()
    user = extract_link("https://www.linkedin.com/in/fabio-seiki-ishitani-240a3625/")
    
    print('> Extraindo perfíl')
    profile = api.get_profile(user)

    data['Sumário'] = profile["summary"]
    data['Name'] = profile['firstName'] + ' ' + profile['lastName']
    data['Ocupação'] = profile["headline"]
    data['Localização'] = profile["geoLocationName"] + ' ' + profile['locationName']
    
    company_detail = []
    for experience in profile["experience"]:
        print(experience.get("locationName"))
        print(experience.get('companyName'))
        print(experience.get("description"))
        inicio = f"{experience['timePeriod']['startDate']['month']}/{experience['timePeriod']['startDate']['year']}"

        print(inicio)

        print(experience.get("title"))
        print('\n')

    # print(data)

    # print('Escrevendo no arquivo...')
    # save_to_json(profile, 'profile')
    # print('Terminado!')
    # JSONtoExcel('profile')
    #  JSONJ

if __name__ == "__main__":
    main()