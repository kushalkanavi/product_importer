from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import productdetails

from celery import shared_task

@shared_task
def uploadFile(request):
    user = User.objects.get(id=request.user.id)

    csv_file = request.FILES.get('productfile')

    import pandas as pd
    df = pd.read_csv(csv_file, index_col=False)

    for index, item in df.iterrows():
        name = item['name']
        sku = item['sku']
        desc = item['description']

        if productdetails.objects.filter(sku=sku).exists():
            productdetails.objects.filter(sku=sku).update(name=name,
                                                          description=desc,
                                                          created_by=user)

        else:
            productdetails.objects.create(name=name,
                                          sku=sku,
                                          description=desc,
                                          created_by=user)

    return render(request, 'myApp/main.html')