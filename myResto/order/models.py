from django.db import models
import json
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os


# Create your models here.
class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField()

@receiver(post_delete, sender=MenuItem)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(pre_save, sender=MenuItem)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_image = MenuItem.objects.get(pk=instance.pk).image
        except MenuItem.DoesNotExist:
            return
        else:
            new_image = instance.image
            if old_image and old_image != new_image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

class Cart(models.Model) :
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255)
    items = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=0, max_digits=12)
    sub_total = models.DecimalField(decimal_places=0, max_digits=12)

class Order(models.Model) :
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=12, decimal_places=0)
    status = models.CharField(max_length=255)


class OrderItem(models.Model):
    user = models.CharField(max_length=255)
    order_details = models.JSONField()
    order_status = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)

    def save_order(self, order_details):
        serialized_details = json.dumps(order_details)
        self.order_details = serialized_details
        self.save()

    def get_order_details(self):
        serialized_details = self.order_details
        order_details = json.loads(serialized_details)
        return order_details
