from django.shortcuts import redirect
def Is_tacher(func):
    """
    حتما قبل آن داکراتور login required را قرار دهید
    :param func:
    :return:
    """
    def wrapper(*args,**kwargs):
        request = args[0]
        try:
            if request.user.teacher :
                return func(*args,**kwargs)
        except :
            return redirect("user:profile")

    return wrapper