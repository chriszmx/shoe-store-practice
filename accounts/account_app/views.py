from django.shortcuts import render
from common.json import ModelEncoder
from .models import Customer
from django.http import JsonResponse


class CustomerListEncoder(ModelEncoder):
    model = Customer
    properties = [
        'name',
        'email',
        'address',
    ]


class ShowCustomerEncoder(ModelEncoder):
    model = Customer
    properties = [
        'name',
        'email',
        'address',
    ]


def list_customers(request):
    customers = Customer.objects.all()
    return JsonResponse(
        customers,
        encoder=CustomerListEncoder,
        safe=False,
    )


def show_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    return JsonResponse(
        customer,
        encoder=ShowCustomerEncoder,
        safe=False,
    )
