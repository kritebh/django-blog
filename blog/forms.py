from django import forms
from django.forms import fields, widgets
from .models import Post,Category

choices=Category.objects.all().values_list('name','name')
category_choices_list =[]

for i in choices:
    category_choices_list.append(i)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=category_choices_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(choices=category_choices_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }