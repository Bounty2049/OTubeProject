from django import forms
from products.models import Product, ProductCategory


# class UserCreatingLesson(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('title', 'description', 'preview', 'video', 'category')


class UserCreationLesson(forms.ModelForm):
    # title = forms.CharField(widget=(forms.TextInput(attrs={'placeholder': 'title'})))
    # description = forms.CharField(widget=(forms.Textarea(attrs={'cols': '30', 'row': '10'})))
    # preview = forms.ImageField(widget=(forms.FileInput(attrs={'placeholder': 'image'})))
    # video = forms.FileField(widget=(forms.FileInput(attrs={'placeholder': 'video'})))
    # category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())
    
    class Meta:
        model = Product
        fields = ('title', 'description', 'preview', 'video', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'user-input'}),
            'description': forms.Textarea(attrs={'class': 'user-input', 'cols': '30', 'row': '10'}),
            'preview': forms.FileInput(attrs={'class': 'user-input'}),
            'video': forms.FileInput(attrs={'class': 'user-input'})
        }