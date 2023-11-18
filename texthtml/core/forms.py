from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

class PostText(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")

    class Meta:
        model = TextHtml
        fields = ('body',)