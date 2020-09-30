from django.db import models
from django.utils import timezone


class DataSet(models.Model):
    input_file = models.FileField(
        verbose_name='input file')
    result_graph = models.ImageField(
        verbose_name='result graph')
    created_at = models.DateTimeField(
        blank=True, null=True)

    def save(self, *args, **kwargs):
        now = timezone.now()

        if self.created_at is None:
            self.created_at = now

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'data set'
        verbose_name_plural = 'data sets'