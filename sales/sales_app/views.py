from django.shortcuts import render
from .common.json import ModelEncoder
from .models import ShoeInventory, ShoppingCart
from django.http import JsonResponse


class CartListEncoder(ModelEncoder):
    model = ShoppingCart
    properties = [
        'created_at',
        'updated_at',
    ]


class CartDetailEncoder(ModelEncoder):
    model = ShoppingCart
    properties = [
        'created_at',
        'updated_at',
    ]


class ShoeDetailEncoder(ModelEncoder):
    model = ShoeInventory
    properties = [
        'name',
        'image',
        'size',
        'brand',
        'color',
        'price',
        'quantity',
        'description',
        'sku',
    ]


class ShoesListEncoder(ModelEncoder):
    model = ShoeInventory
    properties = [
        'name',
        'image',
        'description',
        'brand',
        'price',
    ]


def list_shoes(request):
    shoes = ShoeInventory.objects.all()
    return JsonResponse(list(shoes), encoder=ShoesListEncoder, safe=False)


def shoe_detail(request, pk):
    shoe = ShoeInventory.objects.get(id=pk)
    return JsonResponse(
        shoe,
        encoder=ShoeDetailEncoder,
        safe=False,
    )


def cart_list(request):
    cart = ShoppingCart.objects.all()
    return JsonResponse(
        cart,
        encoder=CartListEncoder,
        safe=False,
    )


def cart_detail(request, pk):
    cart = ShoppingCart.objects.filter(id=pk)
    return JsonResponse(
        cart,
        encoder=CartDetailEncoder,
        safe=False,
    )
