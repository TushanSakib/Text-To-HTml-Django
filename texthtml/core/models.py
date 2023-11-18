from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class TextHtml(models.Model):
    body = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.models.DateField(_(""), auto_now=True, auto_now_add=True)
    