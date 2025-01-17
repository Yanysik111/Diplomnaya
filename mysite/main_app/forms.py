from django import forms
from .models import Text


class TextForm(forms.ModelForm):
    """
    Форма для добавления нового текста.

    Поля:
        text (CharField): Поле для ввода текста.
    """

    class Meta:
        model = Text
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }




