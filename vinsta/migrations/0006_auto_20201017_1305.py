# Generated by Django 3.1.2 on 2020-10-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinsta', '0005_auto_20201017_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='vik.jpg', upload_to='photos/'),
        ),
    ]