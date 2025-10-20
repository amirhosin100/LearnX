from django.shortcuts import redirect
from django.core.exceptions import FieldDoesNotExist
from learn.models import Learn
def Is_tacher(func):
    """
    حتما قبل آن داکراتور login required را قرار دهید
    :param func:
    :return :
    """
    def wrapper(*args,**kwargs):
        request = args[0]
        try:
            if request.user.teacher :
                return func(*args,**kwargs)

        except FieldDoesNotExist:
            return redirect("user:profile")

    return wrapper

def checking_learn(func):
    """
    این تابع برسی می کند که آیا این کاربری که درخواست ارسال کرده است مدرس دوره است یا نه
    :param func:
    :return:
    """
    def wrapper(*args,**kwargs) :
        request = args[0]
        id = kwargs["id"]
        learn = Learn.objects.get(id=id)
        try :
            teacher = request.user.teacher
        except FieldDoesNotExist :
            return redirect("user:profile")
        else:
            if learn.teacher == teacher or request.user.is_superuser:
                return func(*args,**kwargs)
        return redirect("user:profile")
    return wrapper