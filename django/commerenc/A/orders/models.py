from django.db import models
from account.models import User
from django.conf import settings
from django.contrib.auth import get_user_model #the active User
from home.models import Product


class Order(models.Model):
   #user = models.ForeignKey(User)
   #user = models.ForeignKey(settings.AUTH_USER_MODEL)
   user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE, related_name = 'orders')
   paid = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)

   class Meta:
       ordering = ('paid','-updated') #first which are paid and then not paid and also -updated : the newsest updated

   def __str__(self):
       return f'{self.user} - {str(self.id)}'

   def get_total_price(self):
       return sum(item.get_cost() for item in self.items.all()) #items is the related name

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name = 'items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name = 'order_items')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity