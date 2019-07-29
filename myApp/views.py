from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect ,HttpResponse
from django.urls import reverse, reverse_lazy
from django import forms
from .forms import ProductForm
from .models import productdetails
import datetime

import json
from django.http import JsonResponse
from django.core import serializers

from django.db.models import Q
from django.contrib import messages
from django.views.decorators.http import require_http_methods

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myApp/index.html')


class main(View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()

        product_details = serializers.serialize('json', productdetails.objects.all())
        product__data = [d['fields'] for d in json.loads(product_details)]
        product_details_id = [d['pk'] for d in json.loads(product_details)]

        data = zip(product_details_id, product__data)

        context = {
            'form'	: form,
            'data'	: data,
            }

        return render(request, 'myApp/main.html', context)


# class uploadFile(View):
#     def post(self, request, *args, **kwargs):
#         user = User.objects.get(id=request.user.id)
#
#         csv_file = request.FILES.get('productfile')
#
#         import pandas as pd
#         df = pd.read_csv(csv_file, index_col=False)
#
#         for index, item in df.iterrows():
#             name = item['name']
#             sku = item['sku']
#             desc = item['description']
#
#             if productdetails.objects.filter(sku=sku).exists():
#                 productdetails.objects.filter(sku=sku).update(name=name,
#                                                               description=desc,
#                                                               created_by=user)
#
#             else:
#                 productdetails.objects.create(name=name,
#                                               sku=sku,
#                                               description=desc,
#                                               created_by=user)
#
#         return render(request, 'myApp/main.html')

def productSearch(request):
    if request.method == 'POST':
        srch = request.POST['search']

        if srch:
            match = productdetails.objects.filter(Q(sku__icontains=srch) | Q(name__icontains=srch) |
                                                  Q(description__icontains=srch) | Q(status=srch))

            if match:
                form = ProductForm()
                product_details = serializers.serialize('json', match)
                product__data = [d['fields'] for d in json.loads(product_details)]
                product_details_id = [d['pk'] for d in json.loads(product_details)]

                data = zip(product_details_id, product__data)

                context = {
                    'srch': data,
                    'form': form,
                }
                return render(request, 'myApp/main.html', context)
            else:
                messages.error(request, 'No Result Found.')

        else:
            return render(request, 'myApp/main.html')

    return render(request, 'myApp/main.html')

class addProduct(View):
    def post(self, request, *args, **kwargs):
        form = ProductForm(self.request.POST)
        if form.is_valid():
            fform = form.save()
            productdetails.objects.filter(product_id=fform.product_id).update(created_by=request.user.id)

        return redirect('intro:main')


class editProduct(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs['id']

        form = ProductForm(instance=productdetails.objects.get(product_id=product_id))
        context = {
            'product_id': product_id,
            'form': form}

        return render(request, 'myApp/product_edit.html', context)


    def post(self, request, *args, **kwargs):
        product_id = kwargs['id']

        form = ProductForm(self.request.POST, instance=productdetails.objects.get(product_id=product_id))
        if form.is_valid():
            form.save()
        return redirect('intro:main')

class deleteSingleProduct(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs['id']
        productdetails.objects.filter(product_id=product_id).delete()

        return redirect('intro:main')

class deleteAllProduct(View):
    def get(self, request, *args, **kwargs):
        productdetails.objects.all().delete()

        return redirect('intro:main')

def stream(request):
    return HttpResponse(
        'data: The server time is: %s\n\n' % datetime.datetime.now(),
        content_type='text/event-stream'
    )
