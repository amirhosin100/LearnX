from learn.models import Learn
from django.contrib import messages
from django.shortcuts import redirect

# decorator for checking (register in learn) or not
def checking_register_learn(func):
    def wrapper(*args,**kwargs):
        request = args[0]
        slug_learn = kwargs["slug_learn"]
        learn = Learn.objects.get(slug=slug_learn)
        if learn in request.user.learns.all() :
            return func(*args,**kwargs)
        else:
            messages.error(request, "لطفا در دوره شرکت کنید!")
            return redirect("learn:learn_detail",slug_learn=slug_learn)
    return wrapper