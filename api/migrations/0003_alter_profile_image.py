# Generated by Django 3.2.5 on 2022-07-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220702_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='media/profile/placeholder.png', null=True, upload_to='media/profile/'),
        ),
    ]
