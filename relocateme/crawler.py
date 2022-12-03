from bs4 import BeautifulSoup


def relocatme_crawler(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    jobs = soup.find_all('div', class_='jobs-list__job')
    job_count = 0
    all_jobs = []
    for job in jobs:
        job_name = job.find(class_="job__title").get_text()
        job_content = job_name.strip('\n').split('\n')
        job_title = job_content[0]
        try:
            job_location = job_content[1]
        except:
            job_location = 'Relocation or remote'
        job_preview = job.find(class_="job__preview").get_text()
        job_info = job.find(class_="job__info")
        job_company = job_info.find(class_="job__company").get_text().strip('\n')
        try:
            relocation_info = job_info.find(class_='relocation-package-wrapper').find_all('div')
            relocation_type = relocation_info[0].get_text().strip('\n')
            relocation_details = relocation_info[1].get_text().strip('\n').split('\n\n\n\n')
        except:
            relocation_type = 'Advanced relocation package'
            relocation_details = 'Unknown'

        job_tags = job.find(class_="job__tags_wrapper").get_text().strip('\n').split('\n')
        link = 'https://relocate.me/' + job.find(class_="job__title").find('a').attrs['href']
        try:
            job_image = job.find(class_="job__title").find(class_='company-logo').find('img').attrs['data-src'].split('/')[-1]
            logo = 'https://relocate.me/uploads/images/companies/' + job_image
        except:
            logo = 'default_image'

        data = {'title': job_title, 'company': job_company, 'location': job_location,
                'preview': job_preview, 'tags': job_tags, 'relocation_type': relocation_type,
                'relocation_details': relocation_details, 'link': link, 'logo': logo}

        all_jobs.append(data)

        job_count += 1

    return job_count, all_jobs



