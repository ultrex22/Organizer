from django.db import models


# Create your models here.


class Notes(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    color = models.CharField(max_length=15,
                             choices=[('red', 'Red'), ('blu', 'Blue'), ('org', 'Orange'), ('pur', 'Purple')])
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
