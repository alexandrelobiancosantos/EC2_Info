from django.urls import path
from EC2_app.views import home, ec2_info

urlpatterns = [
    path('', home, name='home'),
    path('ec2_info/', ec2_info, name='ec2_info'),
]