from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'EC2_app/home.html')


def ec2_info(request):
    return render(request, 'EC2_app/ec2_info.html')