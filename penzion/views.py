from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class OkoliView(TemplateView):
    template_name = 'okoli.html'


class KontaktView(TemplateView):
    template_name = 'kontakt.html'


class CenikView(TemplateView):
    template_name = 'cenik.html'


class PokojeView(TemplateView):
    template_name = 'pokoje.html'


class FotogalerieView(TemplateView):
    template_name = 'fotogalerie.html'
