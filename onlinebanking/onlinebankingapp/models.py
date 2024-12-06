import random
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    account_number = models.CharField(max_length=10, unique=True, default=''.join([str(random.randint(0, 9)) for _ in range(10)]))
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)  # 'deposit' or 'withdraw'
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Complaints(models.Model):
    custmoer_name = models.CharField(max_length=50,unique=True)
    email = models.EmailField()
    complaint_text = models.TextField()
    
    def __str__(self):
        return self.custmoer_name
        
    