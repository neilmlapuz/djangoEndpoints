from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from customer.models import Customer
from django.core import serializers
import json


@csrf_exempt 
def index(request):
    if(request.method == "GET"):
        all_objects = [*User.objects.all(), *Customer.objects.all()]
        customerJson = serializers.serialize('json', all_objects)

        # print(customerJson)
        customerJson = json.loads(customerJson)
        for customer in customerJson:
            print(customer)

        return HttpResponse(status=200)

        

    elif(request.method == "POST"):
        body = json.loads(request.body.decode('utf-8'))

        name = body['username']
        country = body['country']
        phone = body['phone']


        #test fields
        if not name or not country or not phone:
            return HttpResponse("Some Are Fields not satisfied\n", status=400)


        #assume that a user is a customer
        user = User(username=name)
        user.save()


        #test country check
        if not checkCountry(body['country']):
            return HttpResponse("Country not found\n", status=400)
        
        
        cus = Customer(user=user, country=country, phone=phone)
        cus.save()

        return HttpResponse("Saved \n")


#small country check 
def checkCountry(inputCountry):
    countries = ["Ireland","Germany","Portugal","Spain","Maldova","France"]
    
    return True if inputCountry in countries else False



