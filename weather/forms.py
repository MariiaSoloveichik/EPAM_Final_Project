from django import forms
from functools import partial

DateInput = partial(forms.DateInput, {"class": "datepicker"})


class CityForm(forms.Form):
    city_choices = (
        ("Saint Petersburg", "Saint Petersburg"),
        ("Orenburg", "Orenburg"),
        ("Krasnodar", "Krasnodar"),
        ("Murmansk", "Murmansk"),
        ("Vladivostok", "Vladivostok"),
        ("Sochi", "Sochi"),
        ("Rome", "Rome"),
        ("London", "London"),
        ("Paris", "Paris"),
        ("Barcelona", "Barcelona"),
        ("Canberra", "Canberra"),
    )

    form_city = forms.ChoiceField(
        label="City",
        choices=city_choices,
        initial="",
        widget=forms.Select(),
        required=True,
    )


class StartDateForm(forms.Form):
    form_start_date = forms.DateField(
        label="from", required=True, widget=DateInput(), input_formats=["%d-%m-%Y"]
    )


class EndDateForm(forms.Form):
    form_end_date = forms.DateField(
        label="to", required=True, widget=DateInput(), input_formats=["%d-%m-%Y"]
    )
