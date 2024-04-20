from django.db.models import Q
from goods.models import Categories, Products

def catalog(request):
    catalog = Categories.objects.all()
    return {'catalog': catalog}

def action(request):
    action = Products.objects.filter(~Q(discount=0.00))
    print(action)
    return {'action': action}