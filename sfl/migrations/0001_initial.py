# Generated by Django 2.2.11 on 2020-03-29 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sflOrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesOrderNo', models.CharField(max_length=20)),
                ('offerName', models.CharField(max_length=20)),
                ('subRefId', models.CharField(max_length=20)),
                ('subscriptionId', models.CharField(max_length=20)),
                ('prov_email', models.EmailField(max_length=254)),
                ('deliveryMethod', models.CharField(max_length=10)),
                ('sflProvStatus', models.CharField(max_length=10)),
            ],
        ),
    ]
