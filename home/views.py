from django.shortcuts import render, HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')