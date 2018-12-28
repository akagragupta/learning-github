from django.shortcuts import render
from django.http import HttpResponse
#from AppTwo.models import User
from AppTwo.forms import Modelform
# Create your views here.
def index(request):
	return render(request,'AppTwo/index.html')
	

def help(request):
	helpdict={'help_insert':'HELP PAGE'}
	return render(request,'AppTwo/help.html',context=helpdict)
	

def form(request):
	form= Modelform()

	if request.method == "POST":
		form= Modelform(request.POST)

		if form.is_valid:
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR")

	return render(request,'AppTwo/user.html',context={'form':form})