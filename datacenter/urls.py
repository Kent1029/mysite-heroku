"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mysite import views

urlpatterns = [
	path('logout/',views.mylogout),
	path('note/',views.note),
	path('addnote/',views.addnote),
	path('chart/',views.chart),
	path('rank/',views.rank),
	path('show/<int:id>/',views.show), #show文章
	path('delete/<int:id>/',views.delete), #刪除文章
	path('deletenote/<int:id>/',views.deletenote),
	path('news/', views.news),
	path('', views.index),
	path('admin/', admin.site.urls),
]

#在menu.html新增連結頁面之後需要到這新增path
# 下一步更改views.py