from src.utils.utils import check_param


# Extract JSON
def extract_json_data(profile, url):
    data = dict()
    
    data['Link'] = url
    data['Name'] = profile['firstName'] + ' ' + profile['lastName']
    try:
        data['Sumário'] = profile["summary"]
    
    except KeyError:
        data['Sumário'] = "Não existente!"

    try:
        data['Ocupação'] = profile["headline"]
    
    except KeyError:
        data['Ocupação'] = "Não existente!"

    try:
        data['Localização'] = profile["geoLocationName"] + ' ' + profile['locationName']
    
    except KeyError:
        data['Localização'] = "Não existente!"
    
    # Experiência
    conpany_detail = get_experience(profile)
    data['Empresas'] = '*'.join(conpany_detail)

    # Graduação
    education = get_education(profile)
    data['Educação'] = '*'.join(education)
    
    # certificados 
    
    certificates = get_certificates(profile)
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
        # print(certificates_info)
        certificates.append(certificates_info)

    return certificates
