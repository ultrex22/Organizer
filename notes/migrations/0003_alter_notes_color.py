# Generated by Django 4.0.1 on 2022-01-15 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_notes_id_alter_notes_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='color',
            field=models.CharField(choices=[('rd', 'Red'), ('blu', 'Blue'), ('grn', 'Green'), ('yl', 'Yellow')], max_length=15),
        ),
    ]