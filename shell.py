from my_app.models import *

user1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
client = Client.objects.create(name="Azat Sokolov", card_number='4147 5657 9878 9009', user=user1)
user2 = User.objects.create(email='altywa1998@gmail.com', password='nono34')
worker = Worker.objects.create(name="Altynai Alieva", position="Cashier", user=user2)

sha = Food.objects.create(name="Shawarma", start_price=50)
hamb = Food.objects.create(name="Hamburger", start_price=25)

cheese = Ingredient.objects.create(name="Cheese", extra_price=10)
chicken = Ingredient.objects.create(name="Chiken", extra_price=70)
cow = Ingredient.objects.create(name="Beef", extra_price=80)
salad = Ingredient.objects.create(name="Salad", extra_price=15)
fries = Ingredient.objects.create(name="Fries", extra_price=15)

sha.extrafood.set([cow, cheese, salad, fries], through_defaults={'client': client, 'worker': worker})
hamb.extrafood.set([chicken, salad], through_defaults={'client': client, 'worker': worker})



