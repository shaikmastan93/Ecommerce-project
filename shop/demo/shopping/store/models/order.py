from django.db import models

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderDetail(models.Model):
    user = models.IntegerField()  # `default=True` doesn't make sense for an integer field
    product_name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    qty = models.PositiveIntegerField(default=1)  # `PositiveField` should be `PositiveIntegerField`
    price = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending', choices=STATUS_CHOICES)
