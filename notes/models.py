from django.db import models



# Create your models here.


class Notes(models.Model):
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    color = models.CharField(max_length=15,
                             choices=[('bg-red-200', 'Red'), ('bg-blue-200', 'Blue'), ('bg-orange-100', 'Orange'),
                                      ('bg-indigo-200', 'Purple')])
    image = models.ImageField(null=True, blank=True, upload_to="note_files")

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
