# Generated by Django 5.0.6 on 2024-10-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.IntegerField()),
                ('item_quantity', models.IntegerField()),
                ('item_description', models.CharField(max_length=100)),
            ],
        ),
    ]
