# Generated by Django 4.0.6 on 2022-08-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_adopt_picupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='lost',
            name='picUpload',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]