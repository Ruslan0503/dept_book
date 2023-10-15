from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    adress = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    password_number = models.CharField(max_length=30, blank=True, null=True)
    dept = models.FloatField(default=0, blank=True) 
    returned_dept = models.FloatField(default=0, blank=True)
    deptor = models.BooleanField(default=False, blank=True)
    dateReturn = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


    @property
    def get_all_dept(self):
        depts = self.orderitem_set.all()
        total = sum([item.get_total for item in depts])
        return total
    
    def get_history(self):
        return self.historyturndept_set.all()


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):
    who = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    # last_update = models.DateTimeField(auto_now=True)
    # returned_dept = models.FloatField(default=0, blank=True)
    # dept = models.FloatField(default=0, blank=True)
    class Meta:
        ordering = ['-id']   

    @property
    def get_all_sum(self):
        depts = self.orderitem_set.all()
        total = sum([item.get_total for item in depts])
        return total     
    
class historyTurnDept(models.Model):
    who = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0, blank=True)
    time = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    who = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    @property
    def get_total(self):
        return self.product.price * self.quantity