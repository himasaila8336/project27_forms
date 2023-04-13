from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic inserted successfully')
    return render(request,'insert_topic.html')