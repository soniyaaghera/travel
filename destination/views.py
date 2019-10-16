from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def destinations(request):
	return render(request, 'destinations.html')

def home(request) :
	return render(request, 'index.html')

