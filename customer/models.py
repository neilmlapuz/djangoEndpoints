from django.db import models
from django.contrib.auth.models import User


# Extension of table -- 1 user will have 1 profile
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    country = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=11)
    # class Meta:
    #     model = User
    #     fields = ('first_name', 'country','phone')



    def __str__(self):
        return "%s %s %s" % (self.user.username, self.country, self.phone)




