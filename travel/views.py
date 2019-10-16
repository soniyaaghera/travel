
from django.shortcuts import render
from .models import Destination

def index(request):

	dests = Destination.objects.all()

	return render(request, "index.html", {'dests' : dests})
# def home(request):
# 	return render(request, 'home.html', {'name' : 'Soniya'})

# def add(request):
# 	val1 = int(request.POST['num1'])
# 	val2 = int(request.POST['num2'])
# 	res = val1 + val2
# 	return render(request, "result.html", {'result' : res})