# Generated by Django 4.0.1 on 2022-01-31 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_notes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notes'),
        ),
    ]
