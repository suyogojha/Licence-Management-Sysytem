# Generated by Django 4.0.3 on 2022-04-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_onlinelicenceform_contactno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinelicenceform',
            name='contactno',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='onlinelicenceform',
            name='officecontactno',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
