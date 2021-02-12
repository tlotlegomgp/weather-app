from django import forms

class SearchForm(forms.Form):
	city_search = forms.CharField(max_length = 35, widget=forms.TextInput(attrs={'class':"form-control", 'name':"city_search", 'required': True, 'placeholder':"Enter City Name", 'style':'border: 1px solid #243E36;'}))
