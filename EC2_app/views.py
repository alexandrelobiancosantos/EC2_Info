from django.shortcuts import render
import socket
import platform
# Create your views here.


def home(request):
    return render(request, 'EC2_app/home.html')


def ec2_info(request):
    ip_address = socket.gethostbyname(socket.gethostname())
    os = platform.system()
    # Adicione mais informações de hardware aqui, se necessário

    context = {
        'ip_address': ip_address,
        'os': os,
        # Adicione mais informações de hardware ao contexto aqui
    }

    return render(request, 'EC2_app/ec2_info.html', context)