from django.db import models

# Create your models here.
class Order(models.Model):
	qty_ordered = models.IntegerField()
	total_price = models.DecimalField(decimal_places=2, max_digits=10)
	shipping = models.DecimalField(decimal_places=2, max_digits=10)
	status = models.CharField(max_length=50)
	ordered_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class User_shipping(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=255)
	address2 = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=50)
	zipcode = models.IntegerField()
	# email = models.CharField(max_length=45)
	# password = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	order = models.ForeignKey(Order, related_name="users_shipping")

class User_billing(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	address = models.CharField(max_length=255)
	address2 = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=50)
	zipcode = models.IntegerField()
	card = models.IntegerField()
	cvv = models.IntegerField()
	users_shipping = models.ManyToManyField(User_shipping, related_name="users_billing")
	order = models.ForeignKey(Order, related_name="users_billing")

class Product(models.Model):
	name = models.CharField(max_length=255)
	category = models.CharField(max_length=50)
	desc = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=10)
	inventory = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	order = models.ForeignKey(Order, related_name="products")

