from bs4 import BeautifulSoup


def expatica_crawler(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    jobs = soup.find_all('div', class_='job-item')
    job_count = 0
    all_jobs = []
    for job in jobs:
        job_title = job.find(class_="job-item__title").get_text().strip('\n').strip(' ')
        job_info = job.find(class_="job-item__content").get_text().strip('\n').strip(' ')
        job_location = job.find(class_="job-item__city").get_text().strip('\n').strip(' ')
        link = job.find(class_="job-item__title").find('a').attrs['href']
        logo = 'https://www.expatica.com/app/uploads/2020/08/Expatica-Logo-600-e1587657023471-1.png'
        try:
            job_category = job.find(class_="job-item__category").get_text().strip('\n').strip(' ')

        except:
            job_category = 'Django Python'

        data = {'title': job_title, 'location': job_location,
                'preview': job_info, 'tags': job_category, 'link': link, 'logo': logo}

        all_jobs.append(data)

        job_count += 1

    return job_count, all_jobs



