from django.db import models


class Client(models.Model):
    name_client = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name_client


class Product(models.Model):
    name_product = models.CharField(max_length=50)
    description_product = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_add_product = models.DateField(auto_now_add=True)
    image_product = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name_product


class Order(models.Model):
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    date_create_order = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f' №Заказа: {self.id}  от {self.date_create_order}  клиент: {self.buyer.name_client}'
