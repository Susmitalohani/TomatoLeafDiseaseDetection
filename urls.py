"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myproject.views import home
from Myproject.views import leafImage
from django.conf.urls.static import static
from django.conf import settings
from Myproject.views import submit_feedback
from Myproject.views import view_graph
from Myproject.views import view_conv2d_matrix
from Myproject.views import view_resnet_graph
from Myproject.views import view_conv2d_graph
from Myproject.views import view_model_detail
urlpatterns = [
    path('admin/', admin.site.urls),
path('',home,name ="home"),
path('result',leafImage,name="result"),
path('feedback',submit_feedback,name="feedback"),
path('resnet_cm',view_graph,name="resnet_cm"),
path('conv2d_cmn',view_conv2d_matrix,name="conv2d_cmn"),
path('resnet_acc',view_resnet_graph,name="resnet_acc"),
path('conv2d_acc',view_conv2d_graph,name="conv2d_acc"),
path('allresult',view_model_detail,name="allresult")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)