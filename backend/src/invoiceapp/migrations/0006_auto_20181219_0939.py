# Generated by Django 2.1.3 on 2018-12-19 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0005_a_b'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b',
            name='a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoiceapp.A'),
        ),
    ]
