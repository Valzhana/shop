from django import forms


class ProductForm(forms.Form):
    name_product = forms.CharField(max_length=100)
    description_product = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Описание продукта"}))
    cost = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput(attrs={"placeholder": "Изображение продукта"}))


class ChoiceProductById(forms.Form):
    id_product = forms.IntegerField()


class ChoiceProductByClientBydays(forms.Form):
    id_client = forms.IntegerField()
    days = forms.IntegerField()
