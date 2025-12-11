from django import forms

from .models import Movie

import os

class MovieForm(forms.ModelForm):

    class Meta:

        model = Movie

        # fields = ['name','photo','']

        exclude = ['uuid','active_status']

        widgets = {

            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Movie Name'}),

            'photo':forms.FileInput(attrs={'class':'form-control'}),

            'description':forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Enter Movie Description'}),

            'release_date' :forms.DateInput(attrs={'class':'form-control','type':'date'}),

            'industry' :forms.Select(attrs={'class':'form-select'}),

            'runtime' :forms.TimeInput(attrs={'class':'form-control'},format='H i'),

            'certification' :forms.Select(attrs={'class':'form-select'}),

            'gener' :forms.SelectMultiple(attrs={'class':'form-select'}),

            'artists' :forms.SelectMultiple(attrs={'class':'form-select'}),

            'video' :forms.TextInput(attrs={'class':'form-control','type':'url','placeholder':'Enter Vedio URL'}),

            'tags' :forms.Textarea(attrs={'class':'form-control','rows':3,'placeholder':'Enter Tags With #'}),

            'languages' :forms.SelectMultiple(attrs={'class':'form-select'}),
        }

    def clean(self):

        cleaned_data= super().clean()

        photo = cleaned_data.get('photo')

        if photo and photo.size > 3*1024*1024 :

            self.add_error('photo','maximum file size upto 3 mb')

        