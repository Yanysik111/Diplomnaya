from django.db import models


class Text(models.Model):
    """
    Модель для хранения текста.

    Атрибуты:
        text (TextField): Содержимое текста.
    """

    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.text[:50]