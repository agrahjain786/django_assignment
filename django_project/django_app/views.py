from django.shortcuts import render
from django_app.models import User
# Create your views here.

def index(request):
    return render(request, 'django_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users' : user_list}
    return render(request, 'django_app/user.html',context = user_dict)