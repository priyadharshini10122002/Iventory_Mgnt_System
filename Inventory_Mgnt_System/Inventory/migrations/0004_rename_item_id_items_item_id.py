# Generated by Django 5.0.6 on 2024-10-02 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_alter_items_item_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='item_Id',
            new_name='item_id',
        ),
    ]
