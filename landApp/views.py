from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic, View

class LandView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "landing.html")
