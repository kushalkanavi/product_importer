from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

STATUS = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)

class productdetails(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=True)
    sku = models.CharField(max_length=120, null=True, unique=True)
    description = models.CharField(max_length=255, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUS, default='Active')

    def __str__(self):
        return self.sku
