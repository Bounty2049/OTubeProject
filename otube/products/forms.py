from django import forms
from products.models import Product, ProductCategory


class UserCreatingLesson(forms.Form):

    CATEGORY_CHOICES = ((6, 'Python classic'),
                        (7, 'Django'),
                        (8, 'Request'),
                        (9, 'BeautifulSoup')
                        )

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'description'}))
    preview = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'preview'}), required=False)
    video = forms.FileField(widget=forms.FileInput(attrs={'placeholder': 'video'}), required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    


    class Meta:
        model = Product
        fields = ('title', 'description', 'preview', 'video', 'category')