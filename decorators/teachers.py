from django.shortcuts import redirect
from django.core.exceptions import FieldDoesNotExist,ObjectDoesNotExist
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

        except FieldDoesNotExist and ObjectDoesNotExist:
            return redirect("user:profile")

    return wrapper
