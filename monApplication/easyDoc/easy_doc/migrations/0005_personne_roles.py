# Generated by Django 3.2.19 on 2023-06-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_doc', '0004_rename_my_checkbox_personne_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='roles',
            field=models.CharField(choices=[('SAA', 'SAA'), ('medecin', 'medecin')], default='SAA', max_length=20),
        ),
    ]