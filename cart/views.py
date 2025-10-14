from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .cart import Cart
from learn.models import Learn,RegisterLearn
from django.views.decorators.http import require_POST
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

@require_POST
def buy(request):
    cart = Cart(request)

    user = request.user
    final_price = cart.get_final_price()
    if final_price == 0 :
        for item in cart :
            RegisterLearn.objects.create(user_from=user,learn_to=item["learn"])
        return redirect("user:profile")
    else:
        return redirect("cart:index")
