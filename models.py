from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.name
    

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]

    order_number = models.CharField(max_length=10, unique=True)
    total_items = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    is_ready_notification_sent = models.BooleanField(default=False)

    @classmethod
    def create_order(cls, total_items, total_price, user):
        order_number = cls.generate_order_number()
        return cls.objects.create(order_number=order_number, total_items=total_items, total_price=total_price, user=user)

    @staticmethod
    def generate_order_number():
        return str(uuid.uuid4())[:10]  # Generate a random UUID and take the first 10 characters

# This signal handler sends a notification to the user when an order is marked as ready
@receiver(post_save, sender=Order)
def send_order_ready_notification(sender, instance, **kwargs):
    if instance.status == 'ready' and not instance.is_ready_notification_sent:
        # Send notification to user (e.g., email, push notification, etc.)
        # You can use a third-party service or Django's built-in email functionality
        print(f"Order {instance.order_number} is ready. Sending notification to {instance.user.username}")
        instance.is_ready_notification_sent = True
        instance.save()

class AdminNotification(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    is_ready = models.BooleanField(default=False)