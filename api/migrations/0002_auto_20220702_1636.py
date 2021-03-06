# Generated by Django 3.2.5 on 2022-07-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.FileField(null=True, upload_to='media/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='people_helped',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
