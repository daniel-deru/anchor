from django.db import models


class ShoppingList(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

class ShoppingListItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    planned = models.BooleanField(default=False)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
