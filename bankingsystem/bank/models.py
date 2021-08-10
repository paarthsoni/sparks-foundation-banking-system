from django.db import models

import datetime
from datetime import datetime
class customer(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    currentbalance=models.CharField(max_length=122)

    def __str__(self):
        return self.name
    

class transferhistory(models.Model):
    sender=models.CharField(max_length=122)
    receiver=models.CharField(max_length=122)
    amount=models.CharField(max_length=122)
    semail=models.CharField(max_length=122,null=True, blank=True)
    remail=models.CharField(max_length=122,null=True, blank=True)
    
    
    def __str__(self):
        return self.sender +" "+ "to" + " " + self.receiver 
