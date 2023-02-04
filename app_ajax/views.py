from django.http import JsonResponse
from django.shortcuts import render

from app_ajax.models import AllUser

def index(request):
    return render(request, 'index.html', {'all_data': AllUser.objects.all()})

def add_data(request):
    AllUser.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        mobile = request.POST['mobile'],
    )
    all_obj = list(AllUser.objects.values()) #all rows get hogi but special JS ke liye
    return JsonResponse({'all_data':all_obj})


def delete_row(request):
    row_obj = AllUser.objects.get(id=  request.POST['id'])
    row_obj.delete()

    all_users = list(AllUser.objects.values())
    return JsonResponse({'all_data': all_users })