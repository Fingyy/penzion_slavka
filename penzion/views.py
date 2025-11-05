import logging
from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView
from django.conf import settings
from django.urls import reverse_lazy

from penzion.forms import ReservationForm

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


class ReservationView(FormView):
    template_name = 'rezervace.html'
    form_class = ReservationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        data = form.cleaned_data
        subject = "Nová rezervace z webu penzionu"
        message = (
            f"Jméno: {data['first_name']}\n"
            f"Příjmení: {data['last_name']}\n"
            f"Adresa: {data['address']}\n"
            f"PSČ: {data['postal_code']}\n"
            f"Město: {data['city']}\n"
            f"E-mail: {data['email']}\n"
            f"Telefon: {data['phone']}\n"
            f"Datum příjezdu: {data['arrive_date']}\n"
            f"Datum odjezdu: {data['departure_date']}\n"
            f"Počet nocí: {data['no_of_nights']}\n"
            f"Počet dospělých: {data['no_of_adults']}\n"
            f"Počet dětí: {data['no_of_kids'] or 0}\n"
            f"Počet pokojů: {data['no_of_rooms']}\n"
            f"Typ pokoje: {data['room_type']}\n"
            
            f"Zpráva: {data['description'] or '(žádná)'}"
        )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [tova.tremosnice@seznam.cz]  # příjemnce objednávek
        )
        return super().form_valid(form)



