from django.shortcuts import render

from storeroom.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse


from barcode.writer import ImageWriter


import json
import os
import barcode
import jdatetime


# Create your views here.
def index(request):
    return render(request, 'storeroom/index.html')


@login_required
def input_record(request):
    return render(request, 'storeroom/dashboard-add-listing.html')


@login_required
def search_record(request):
    return render(request, 'storeroom/search.html')


@login_required
def update_record(request):
    return render(request, 'storeroom/update.html')


@login_required
def report(request):
    return render(request, 'storeroom/search.html')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required
def register(request):
    if request.method == 'POST' and is_ajax(request=request):
        proje_name = request.POST.get('proj_name')
        cat = request.POST.get('category')
        devtype = request.POST.get('device_type')
        devmileage = request.POST.get('device_mil')
        devbrand = request.POST.get('device_brand')
        devstat = request.POST.get('device_stat')
        descrip = request.POST.get('description')
        file_1 = request.POST.get('file1')
        file_2 = request.POST.get('file2')
        file_3 = request.POST.get('file3')
        file_4 = request.POST.get('file4')
        file_5 = request.POST.get('file5')
        file_6 = request.POST.get('file6')
        fullname = request.POST.get('name')
        proje_id = request.POST.get('proj_id')
        time = request.POST.get('time')
        timedes = request.POST.get('timedesc')
        status = 1

        if not Project.objects.filter(project_name=proje_name).exists():
            project_instance = Project.objects.create(project_name=proje_name, project_id=proje_id)
        else:
            project_instance = Project.objects.get(project_name=proje_name)
        product_instance = Product.objects.create(name=fullname,
                                                  project_id=project_instance.project_id,
                                                  category=cat,
                                                  device_type=devtype,
                                                  device_status=devstat,
                                                  device_brand=devbrand,
                                                  device_mileage=devmileage,
                                                  description=descrip,
                                                  image_1=file_1,
                                                  image_2=file_2,
                                                  image_3=file_3,
                                                  image_4=file_4,
                                                  image_5=file_5,
                                                  image_6=file_6,
                                                  )
        barimage = barcode.Code128(str(product_instance.pid), writer=ImageWriter())
        barimage.save('image {}'.format(product_instance.pid))
        # os.startfile(f'image {product_instance.pid}', 'print')
        # physical_print(f'image {product_instance.pid}.png')
        os.remove(f'image {product_instance.pid}.png')
        Status.objects.create(pid=product_instance, time=time, status=status, desc=timedes)

        id1 = product_instance.pid
        return HttpResponse(json.dumps({'id': id1}), content_type="application/json")
    else:
        response = HttpResponse(json.dumps({'error': 'Bad request receive. Sorry!'}), content_type='application/json')
        response.status_code = 400
        return response


@login_required
def search_status(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        product = Product.objects.get(pid=pid)
        status = Status.objects.filter(pid=pid).order_by('-time')[:1][0]
        project1 = Project.objects.get(project_id=product.project_id)
        pid1 = product.pid
        name = product.name
        projectname = project1.project_name
        type = product.device_type
        mil = product.device_mileage
        brand = product.device_brand
        stat = product.device_status
        timestatus = status.status
        des_time = status.desc
        time = status.time
        return HttpResponse(json.dumps(
            {'pid1': pid1, 'name': name, 'projectname': projectname, 'type': type, 'mil': mil, 'brand': brand,
             'statusproduct': timestatus, 'destime': des_time, 'time': time, 'stat': stat}),
            content_type="application/json")
    else:
        response = HttpResponse(json.dumps({'error': 'Bad request receive. Sorry!'}), content_type='application/json')
        response.status_code = 400
        return response


@login_required
def update_status(request):
    if request.method == 'POST':
        product_id = request.POST.get('pid')
        if Product.objects.filter(pid=product_id).exists():
            product_instance = Product.objects.get(pid=product_id)
        status = request.POST.get('value')
        description = request.POST.get('desc')
        fa_date = jdatetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Status.objects.create(pid=product_instance, time=fa_date, status=status, desc=description)
        response = HttpResponse('')
        response.status_code = 200
        return response
    else:
        response = HttpResponse(json.dumps({'error': 'Bad request receive. Sorry!'}), content_type='application/json')
        response.status_code = 400
        return response


@login_required
def reporting(request):
    status_dict = {'1': 'ورود', '2': 'خروج موقت', '3': 'خروج دائم'}
    secondary_lst = []
    if request.method == 'POST':
        pid = request.POST.get('pid')
        product = Product.objects.get(pid=pid)
        stat2 = list(item[0] for item in Status.objects.values_list('status').filter(pid=pid))
        for i in stat2:
            secondary_lst.append(status_dict[i])
        zaman = list(item[0] for item in Status.objects.values_list('time').filter(pid=pid))
        desc = list(item[0] for item in Status.objects.values_list('desc').filter(pid=pid))
        project = Project.objects.get(project_id=product.project_id)
        pid2 = product.pid
        name = product.name
        cat = product.category
        des = product.description
        type = product.device_type
        model = product.device_status
        brand = product.device_brand
        mil = product.device_mileage
        projectname = project.project_name
        return HttpResponse(json.dumps(
            {'aid2': pid2, 'name': name, 'type': type, 'model': model, 'brand': brand, 'cat': cat,
             'des': des, 'mil': mil, 'projectname': projectname, 'zaman': zaman,
             'desc': desc, 'stat': secondary_lst}), content_type="application/json")

    else:
        response = HttpResponse(json.dumps({'error': 'Bad request receive. Sorry!'}), content_type='application/json')
        response.status_code = 400
        return response


def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse(request.GET.get('next')))
    else:
        messages.info(request, "Please login to access this page.")
        return HttpResponseRedirect(reverse('storeroom:index'))


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        request.user = user
        if user != None:
            login(request, user)
            return redirect(reverse("storeroom:input"), request=request)
        else:
            messages.error(request, "لطفا اطلاعات ورود را به درستی وارد کنید.")
            return HttpResponseRedirect('/')


def logoutuser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')
