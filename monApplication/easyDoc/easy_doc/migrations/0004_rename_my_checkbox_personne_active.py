# Generated by Django 3.2.19 on 2023-06-12 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy_doc', '0003_personne_my_checkbox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personne',
            old_name='my_checkbox',
            new_name='active',
        ),
    ]