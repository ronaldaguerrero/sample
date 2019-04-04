from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First name should be at least 2 characters"
        if postData['fname'].isalpha() == False:
            errors['fname'] = "First name must have only letters"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last name should be at least 2 characters"
        if postData['lname'].isalpha() == False:
            errors['lname'] = "Last name must have only letters"
        users_with_email = User.objects.filter(email=postData['email'])
        if len(users_with_email) > 0:
            errors['email'] = "Email is taken"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is invalid email format"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['conf_password']:
            errors['password'] = "Password must match password confirmation"
        return errors
    def validate_login(self, postData):
        errors = {}
        users_with_email = User.objects.filter(email=postData['email'])
        if len(users_with_email) < 1:
            errors['users_with_email'] = "Invalid Login Information"
        else:
            found_user = users_with_email[0]
            result = bcrypt.checkpw(postData['password'].encode(), found_user.password.encode())
            if result == False:
                errors['users_with_email'] = "Invalid Login Information"
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=255)
    objects = UserManager()

class Order(models.Model):
	total_price = models.DecimalField(decimal_places=2, max_digits=10, default=None, null=True)
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
	size = models.CharField(max_length=2, null=True, default=None)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	order = models.ManyToManyField(Order, related_name="products")

