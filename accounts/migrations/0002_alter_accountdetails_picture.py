# Generated by Django 4.2.1 on 2023-07-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetails',
            name='picture',
            field=models.FileField(blank=True, default='qww.png', null=True, upload_to='account_pictures/'),
        ),
    ]