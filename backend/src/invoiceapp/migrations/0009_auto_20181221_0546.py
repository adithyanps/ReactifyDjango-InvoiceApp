# Generated by Django 2.1.3 on 2018-12-21 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0008_auto_20181219_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='b',
            name='a',
        ),
        migrations.DeleteModel(
            name='A',
        ),
        migrations.DeleteModel(
            name='B',
        ),
    ]
