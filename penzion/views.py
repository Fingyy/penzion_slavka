import logging
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from penzion.forms import RoomTypeForm, OrderForm
from penzion.models import RoomType, Order
from django.urls import reverse_lazy

logger = logging.getLogger(__name__)


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


class RoomTypeCreateView(CreateView):
    template_name = 'rezervace.html'
    model = RoomType
    form_class = RoomTypeForm
    success_url = reverse_lazy('rezervace')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')  # znovu zobrazí stránku s formulářem a chybovými hláškami.
        return super().form_invalid(form)


class OrderCreateView(CreateView):
    template_name = 'rezervace.html'
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('rezervace')

    def form_invalid(self, form):
        logger.warning('User provided invalid data.')
        return super().form_invalid(form)

