from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    extra_price = models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=50)
    start_price = models.IntegerField()
    extrafood = models.ManyToManyField(Ingredient, through='Order')

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'food{self.food} - ing{self.ingredient}, client{self.client}, worker{self.worker}, ' \
               f'dt{self.order_date_time}'
