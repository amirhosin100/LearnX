import json
from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .cart import Cart
from learn.models import Learn,RegisterLearn
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Order,LearnOrder,OffCode
import random
from learn.templatetags import tags,price
# Create your views here.
def index(request):
    cart = Cart(request)
    cart.reget()
    return render(request,"cart.html")

@require_POST
def add_remove_learn_to_cart(request):
    learn_id = request.POST.get("learn_id")
    operation = request.POST.get("operation","add")
    try :
        cart = Cart(request)
        if operation == "add" :
            learn = get_object_or_404(Learn, id=learn_id)
            print("a")
            cart.add_to_cart(learn)
            print("a")
        else:
            cart.remove_from_cart(learn_id)

        return JsonResponse({"success":"Success"})
    except :
        return JsonResponse({"Error":"error"})

@login_required
@require_POST
def buy(request):
    cart = Cart(request)
    user = request.user
    final_price = cart.get_final_price()
    for item in cart :
        RegisterLearn.objects.create(user_from=user,learn_to=item["learn"])

    order = Order.objects.create(user=user, price=0)
    order.save()
    if len(cart.cart.keys()) == 1 :
        description = "خرید دوره ی "
    else:
        description = "خرید دوره های "
    for item in cart :
        description += " | " + item["learn"].title
        LearnOrder.objects.create(learn=item["learn"],order=order)
    order.description = description
    order.save()

    cart.clear()
    return redirect("user:profile")

@require_POST
def set_code(request):

    data = json.loads(request.body)
    code = data.get("code")
    cart = Cart(request)

    def set_context(status):
        percent_off = tags.to_persian_numbers(cart.percent_off)
        price_off = tags.to_persian_numbers(price.point(cart.get_price_off()))
        final_price = cart.get_final_price()
        if final_price == 0:
            final_price = "رایگان"
        else:
            final_price = f"{tags.to_persian_numbers(price.point(cart.get_final_price()))} تومان"

        if status == 200 :
            context = {
                "percent_off": percent_off,
                "price_off": price_off,
                "final_price": final_price,
            }
        else:
            context = {
                "error": "code dose not exist",
                "final_price": final_price,
            }
        return context

    if code :
        if OffCode.objects.filter(code=code).exists() :
            off_code = OffCode.objects.get(code=code)
            cart.set_code(off_code.value)

            return JsonResponse(set_context(200),status=200)
        else:
            cart.set_code(0)
            return JsonResponse(set_context(404),status=404)
    else:
        return  JsonResponse({"error" : "code is empty"},status=400)

