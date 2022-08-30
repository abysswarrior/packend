from django.shortcuts import render, HttpResponse
from django.views import View


class RelocateMeView(View):
    def get(self, request):
        return render(request, 'home/relocateme.html')