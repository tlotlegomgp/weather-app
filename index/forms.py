from django import forms

class SearchForm(forms.Form):
	city_search = forms.CharField(max_length = 35, widget=forms.TextInput(attrs={'class':"form-control", 'name':"city_search", 'required': True, 'placeholder':"Enter city name", 'style':'border-color: #243E36;'}))
