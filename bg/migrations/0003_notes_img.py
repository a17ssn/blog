# Generated by Django 3.0.5 on 2020-05-01 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bg', '0002_auto_20200430_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='img',
            field=models.ImageField(default='', upload_to='img'),
            preserve_default=False,
        ),
    ]