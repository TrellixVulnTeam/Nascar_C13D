# Generated by Django 2.0.6 on 2018-08-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0005_piloto_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='carreras'),
        ),
    ]