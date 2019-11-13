from django.shortcuts import render
from django.views import generic
from .models import Soldado

# Não precisar ser nomeada com 'HomeView'
class QualquerNome(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["soldados"] = Soldado.objects.all()
        return context
# Create your views here.
