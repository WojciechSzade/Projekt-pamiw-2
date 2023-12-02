from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import requests

# Create your views here.
def index(request):
    return render(request, 'webapp/index.html')

def cars_list(request, page=1):
    url = 'http://' + request.get_host() + '/api/car/' + '?page=' + str(page)
    response = requests.get(url)
    context = {
        'cars': response.json()['results'],
        'previous': request.build_absolute_uri(reverse('webapp:cars_list', kwargs={'page': page - 1})) if response.json()['previous']  else None,
        'next': request.build_absolute_uri(reverse('webapp:cars_list', kwargs={'page': page + 1})) if response.json()['next'] else None,
        'page': page
        }
    return render(request, 'webapp/cars_list.html', context=context)

def car_details(request, id):
    url = 'http://' + request.get_host() + '/api/car/' + str(id)
    response = requests.get(url)
    if response.status_code == 404:
        return HttpResponse("ERROR 404 - Car not found")
    print(response.json())
    context = {
        'car': response.json()
    }
    return render(request, 'webapp/car_details.html', context=context)
    
def car_create(request):
    if request.method == 'POST':
        url = 'http://' + request.get_host() + '/api/car/'
        response = requests.post(url, data=request.POST)
        if response.status_code == 201:
            return HttpResponse('Car created successfully')
        else:
            return HttpResponse('Error creating car ' + response.text, status=400)
    else:
        url = 'http://' + request.get_host() + '/api/brand/'
        response = requests.get(url)
        context = {
            'brands': response.json()
        }
        return render(request, 'webapp/car_create.html', context=context)
    
def car_update(request, id):
    if request.method == 'POST':
        url = 'http://' + request.get_host() + '/api/car/' + str(id) + '/'
        response = requests.put(url, data=request.POST)
        if response.status_code == 200:
            return HttpResponse('Car updated successfully')
        else:
            return HttpResponse('Error updating car ' + response.text, status=400)
    else:
        url = 'http://' + request.get_host() + '/api/car/' + str(id)
        response = requests.get(url)
        if response.status_code == 404:
            return HttpResponse("ERROR 404 - Car not found")
        url = 'http://' + request.get_host() + '/api/brand/'
        response_brands = requests.get(url)
        context = {
            'car': response.json(),
            'brands': response_brands.json()
        }
        return render(request, 'webapp/car_update.html', context=context)
    
def car_delete(request, id):
    url = 'http://' + request.get_host() + '/api/car/' + str(id) + '/'
    response = requests.delete(url)
    if response.status_code == 204:
        return HttpResponse('Car deleted successfully')
    else:
        return HttpResponse('Error deleting car ' + response.text, status=400)
    
def brands_list(request, page=1):
    url = 'http://' + request.get_host() + '/api/brand/' + '?page=' + str(page)
    response = requests.get(url)
    context = {
        'brands': response.json()['results'],
        'previous': request.build_absolute_uri(reverse('webapp:brands_list', kwargs={'page': page - 1})) if response.json()['previous']  else None,
        'next': request.build_absolute_uri(reverse('webapp:brands_list', kwargs={'page': page + 1})) if response.json()['next'] else None,
        'page': page
    }
    return render(request, 'webapp/brands_list.html', context=context)

def brand_details(request, name):
    url = 'http://' + request.get_host() + '/api/brand/' + str(name)
    response = requests.get(url)
    if response.status_code == 404:
        return HttpResponse("ERROR 404 - Brand not found")
    context = {
        'brand': response.json()
    }
    return render(request, 'webapp/brand_details.html', context=context)

def brand_create(request):
    if request.method == 'POST':
        url = 'http://' + request.get_host() + '/api/brand/'
        response = requests.post(url, data=request.POST)
        if response.status_code == 201:
            return HttpResponse('Brand created successfully')
        else:
            return HttpResponse('Error creating brand ' + response.text, status=400)
    else:
        return render(request, 'webapp/brand_create.html')
    
def brand_update(request, name):
    if request.method == 'POST':
        url = 'http://' + request.get_host() + '/api/brand/' + str(name) + '/'
        response = requests.put(url, data=request.POST)
        if response.status_code == 200:
            return HttpResponse('Brand updated successfully')
        else:
            return HttpResponse('Error updating brand ' + response.text, status=400)
    else:
        url = 'http://' + request.get_host() + '/api/brand/' + str(name)
        response = requests.get(url)
        if response.status_code == 404:
            return HttpResponse("ERROR 404 - Brand not found")
        context = {
            'brand': response.json()
        }
        return render(request, 'webapp/brand_update.html', context=context)
    
def brand_delete(request, name):
    url = 'http://' + request.get_host() + '/api/brand/' + str(name) + '/'
    response = requests.delete(url)
    if response.status_code == 204:
        return HttpResponse('Brand deleted successfully')
    else:
        return HttpResponse('Error deleting brand ' + response.text, status=400)