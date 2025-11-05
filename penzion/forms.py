from django import forms
from django.utils import timezone


class ReservationForm(forms.Form):
    first_name = forms.CharField(label="Jméno", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Příjmení",
                                max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Adresa", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    postal_code = forms.CharField(label="PSČ",
                                  max_length=5,
                                  widget=forms.TextInput(attrs={"class": "form-control",
                                                                "placeholder": "53843"}))
    city = forms.CharField(label="Město",
                           max_length=50,
                           widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": "Třemošnice"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control",
                                                                           "placeholder": "karel.novak@email.cz"}))
    phone = forms.CharField(label="Telefon", max_length=9, widget=forms.TextInput(attrs={"class": "form-control"}))
    arrive_date = forms.DateField(label="Datum příjezdu",
                                  widget=forms.DateInput(attrs={"type": "date",
                                                                "class": "form-control"}))
    departure_date = forms.DateField(label="Datum odjezdu",
                                     widget=forms.DateInput(attrs={"type": "date",
                                                                   "class": "form-control"}))
    no_of_nights = forms.IntegerField(label="Počet nocí",
                                      min_value=1,
                                      widget=forms.NumberInput(attrs={"class": "form-control"}))
    no_of_adults = forms.IntegerField(label="Počet dospělých osob",
                                      min_value=1,
                                      widget=forms.NumberInput(attrs={"class": "form-control"}))
    no_of_kids = forms.IntegerField(label="Počet dětí od 3 do 12 let",
                                    required=False,
                                    widget=forms.NumberInput(attrs={"class": "form-control"}))
    no_of_rooms = forms.IntegerField(label="Počet pokojů",
                                     min_value=1,
                                     widget=forms.NumberInput(attrs={"class": "form-control"}))
    room_type = forms.ChoiceField(
        label="Typ pokoje",
        choices=[
            ("double_tog", "Dvoulůžkový, postele u sebe"),
            ("double_sep", "Dvoulůžkový, postele odděleně"),
            ("triple", "Třílůžkový"),
            ("quad", "Čtyřlůžkový"),
            ("combination", "Více pokojů uveďte do zprávy")
        ],
        widget=forms.Select(attrs={"class": "form-select"})
    )
    description = forms.IntegerField(label="Zpráva pro penzion",
                                     required=False,
                                     widget=forms.Textarea(attrs={
                                         "rows": 3,
                                         "class": "form-control",
                                         "placeholder": ""
                                     }))

    def clean(self):
        cleaned_data = super().clean()
        arrive_date = cleaned_data.get("arrive_date")
        departure_date = cleaned_data.get("departure_date")
        today = timezone.localdate()

        # Validace datumů
        if arrive_date and arrive_date <= today:
            self.add_error("arrive_date", "Datum příjezdu musí být alespoň zítra.")
        if arrive_date and departure_date and departure_date <= arrive_date:
            self.add_error("departure_date", "Datum odjezdu musí být alespoň den po příjezdu.")
