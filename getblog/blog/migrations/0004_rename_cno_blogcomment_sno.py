# Generated by Django 4.0.4 on 2022-05-24 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='cno',
            new_name='sno',
        ),
    ]