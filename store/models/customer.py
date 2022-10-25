from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password ,check_password


class customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def register(self):
        self.save()

    def customer_exist(self):
        if customer.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def customer_by_email(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False

        


