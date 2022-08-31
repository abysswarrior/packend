from django.shortcuts import render, HttpResponse
from django.views import View
from common.crawler import crawl
import requests


class RelocateMeView(View):
    def get(self, request):
        status = 200
        page_number = 1  # ==> to crawl all pages
        total_job_count = 0
        all_page_data = []
        while True:
            # python jobs link example
            url = f"https://relocate.me/search?query%5B%5D=Python&country%5B%5D=The+Netherlands&time=any&page={page_number}"
            # java jobs link example
            # url = f"https://relocate.me/search?query%5B%5D=Java&country%5B%5D=The+Netherlands&time=any&page={page_number}"
            page = requests.get(url)
            if page.status_code != 200:
                break
            try:
                job_count, all_jobs = crawl(page)
                total_job_count += job_count
                all_page_data += all_jobs
                if job_count == 0:
                    break
            except:
                print(f'can not crawl {url}')
            page_number += 1

        # print(f'Total: {total_job_count} jobs')
        # print(all_page_data)
        return render(request, 'home/relocateme.html', {'jobs_list': all_page_data, 'total_job_count': total_job_count})