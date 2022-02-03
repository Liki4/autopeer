"""autopeer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from peeringmanager.views import *
#from django.contrib.auth.views import login

urlpatterns = [
	path('', PeeringView.as_view(), name='index'),
	path('peerings/<int:pk>/', PeeringDetailView.as_view(), name='peerings-detail'),
	path('peerings/<int:pk>/edit/', UpdatePeeringView.as_view(), name='peerings-edit'),
	path('peerings/new/', CreatePeeringView.as_view(), name='peerings-new'),
	#path('accounts/login/', login, name='login'),
	path('admin/', admin.site.urls),
]
