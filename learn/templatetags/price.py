from django import  template

register = template.Library()

@register.filter(name='point')
def point(value):
    num = ""
    string = list(str(value))
    string.reverse()
    # 100,000
    for i in range(3,len(string),3) :
        string.insert(i,",")
    string.reverse()
    for i in string:
        num += i
    return num

