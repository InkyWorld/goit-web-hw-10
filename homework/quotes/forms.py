from django import forms


class AuthorForm(forms.Form):
    fullname = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "InputFullname"}),
    )
    born_date = forms.DateField(
        label="Born Date",
        widget=forms.DateInput(
            attrs={"class": "form-control", "id": "InputBornDate", "type": "date"}
        ),
    )
    born_location = forms.CharField(
        max_length=200,
        label="Born Location",
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "InputBornLocation"}
        ),
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={"class": "form-control", "id": "InputDescription"}
        ),
    )


class QuoteForm(forms.Form):
    quote = forms.CharField(
        label="Quote",
        widget=forms.Textarea(attrs={"class": "form-control", "id": "InputQuote"})
    )
    author = forms.CharField(
        label="Author",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "InputAuthor"}),
    )
    tags = forms.CharField(
        label="Tags",
        max_length=200,
        widget=forms.HiddenInput(attrs={"class": "form-control", "id": "InputTags"}),
        required=False,
    )