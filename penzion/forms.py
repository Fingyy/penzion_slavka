from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone

# Společný validátor pro jméno a příjmení
name_validator = RegexValidator(
    regex=r'^[A-Ža-ž\s\-]+$',
    message="Pole může obsahovat pouze písmena, mezery a pomlčky."
)


class ReservationForm(forms.Form):
    first_name = forms.CharField(
        label="Jméno",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Karel"
                                      }
                               ),
        validators=[name_validator]  # musí být uvnitř seznamu, proto []
    )
    last_name = forms.CharField(
        label="Příjmení",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Novák"
                                      }
                               ),
        validators=[name_validator]
    )
    address = forms.CharField(
        label="Adresa",
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control",
                                      "placeholder": "Nádražní 1"
                                      }
                               ),
        validators=[RegexValidator(
            regex=r'^[A-Ža-ž0-9\s,.\-\/]+$',
            message="Adresa může obsahovat pouze písmena, čísla a běžné znaky (čárky, tečky, lomítka)."
        )]
    )
    postal_code = forms.CharField(
        label="PSČ",
        min_length=5,
        max_length=6,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "53843"
        }
        ),
        validators=[RegexValidator(
            regex=r'^\d{3}\s?\d{2}$',
            message="PSČ musí být ve formátu 123 45 mebo 12345"
        )]
    )
    city = forms.CharField(
        label="Město",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Třemošnice"
        }
        ),
        validators=[RegexValidator(
            regex=r'^[A-Ža-ž\s\-]+$',
            message="Město může obsahovat pouze písmena a mezery."
        )]
    )
    email = forms.EmailField(
        label="Email",
        error_messages={"invalid": "Neplatný formát pro email.",
                        "required": "Zadejte svůj email."
                        },
        widget=forms.EmailInput(attrs={"class": "form-control",
                                       "placeholder": "karel.novak@email.cz"
                                       }
                                )
    )
    phone = forms.CharField(
        label="Telefon",
        min_length=9,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control"}
                               ),
        error_messages={
            "min_length": "Telefon musí mít alespoň 9 znaků.",
            "required": "Uve%dte prosím svoje telefonní číslo",
        },
        validators=[RegexValidator(regex=r'^\+?\d{9,15}$',
                                   message="Telefon musí obsahovat 9 až 15 číslic, může začínat +."
                                   )
                    ]
    )
    arrive_date = forms.DateField(
        label="Datum příjezdu",
        widget=forms.DateInput(attrs={"type": "date",
                                      "class": "form-control"
                                      }
                               )
    )
    departure_date = forms.DateField(
        label="Datum odjezdu",
        widget=forms.DateInput(attrs={"type": "date",
                                      "class": "form-control"
                                      }
                               )
    )
    # no_of_nights = forms.IntegerField(
    #     label="Počet nocí",
    #     min_value=1,
    #     widget=forms.NumberInput(attrs={"class": "form-control"})
    # )
    no_of_adults = forms.IntegerField(
        label="Počet dospělých osob",
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={"class": "form-control"}
                                 )
    )
    no_of_kids = forms.IntegerField(
        label="Počet dětí od 3 do 12 let",
        required=False,
        initial=0,
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    no_of_rooms = forms.IntegerField(
        label="Počet pokojů",
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    room_type = forms.ChoiceField(
        label="Typ pokoje",
        choices=[
            ("", "Vyberte typ pokoje"),
            ("Dvoulůžkový, postele u sebe", "Dvoulůžkový, postele u sebe"),
            ("Dvoulůžkový, postele odděleně", "Dvoulůžkový, postele odděleně"),
            ("Třílůžkový", "Třílůžkový"),
            ("Čtyřlůžkový", "Čtyřlůžkový"),
            ("Více pokojů uveďte do zprávy", "Více pokojů uveďte do zprávy")
        ],
        widget=forms.Select(attrs={"class": "form-select"})
    )
    description = forms.IntegerField(
        label="Zpráva pro penzion",
        required=False,
        widget=forms.Textarea(attrs={"rows": 3,
                                     "class": "form-control"
                                     }
                              )
    )

    def clean(self):
        cleaned_data = super().clean()
        arrive_date = cleaned_data.get("arrive_date")
        departure_date = cleaned_data.get("departure_date")
        today = timezone.localdate()

        # Validace datumů
        if arrive_date and arrive_date <= today:
            self.add_error("arrive_date", "Datum příjezdu musí být nejdříve následující den.")
        if arrive_date and departure_date and departure_date <= arrive_date:
            self.add_error("departure_date", "Datum odjezdu musí být alespoň den po příjezdu.")
