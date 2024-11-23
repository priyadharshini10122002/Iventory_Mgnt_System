from django.db import models

# Create your models here.
class Items(models.Model):
    item_id=models.IntegerField(null=False,unique=True)
    item_name=models.CharField(max_length=50)
    item_price=models.IntegerField()
    item_quantity=models.IntegerField()
    item_description=models.CharField(max_length=100)
    def __str__(self):
        return self.item_name