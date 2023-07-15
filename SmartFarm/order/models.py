from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.order_number

