from store.models import Product, Customer
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models import F, Func, Value


# Create your views here.


def say_hello(request):
    result = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    context = {
        'name': 'Navid',
        'result': result,
    }
    return render(request, 'hello.html', context)
