
# views.py 是抓檔案的地方
#記得import 模組or資料
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required #登入後才能操作
from django.http import HttpResponse
from django.contrib.auth import logout #登出模組
import random 
from mysite.models import Post,Country,City,Note

#以下三行為繪圖所需模組
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np


def index(request):
	name="黃維毓"
	lotto=[random.randint(1,42) for i in range(6) ]
	special=lotto[0]
	lotto=lotto[1:6]
	x = np.linspace(0, 2*np.pi, 360) #利用np.linspace產生了360個0到2pi之間的數字
	y1 = np.sin(x)            #計算SIN和COS的值，放在y1和y2中，送進Plotly中繪圖
	y2 = np.cos(x)            #完成後，修改index.html 程式碼 
	plot_div = plot([
						go.Scatter(x=x, y=y1,
									mode='lines', name='SIN', 
									text="Title",opacity=0.8, 
									marker_color='blue'),

						go.Scatter(x=x, y=y2,
									mode='lines', name='COS', 
									opacity=0.8, marker_color='green')
						],output_type='div')
	return render(request, "index.html",locals())


def news(request):
	posts=Post.objects.all()
	return render(request, "news.html", locals())

@login_required(login_url="/admin/login/")
def show(request,id):
	try:
		post=Post.objects.get(id=id) #找出符合條件的第一個紀錄
	#posts=Post.objects.filter(id=id) #找出符合條件的所有紀錄
	except:
		return redirect("/news/")
	return render(request, "show.html", locals())

@login_required(login_url="/admin/login/")
def rank(request):
	#rank.html 表單內post傳送資料 處理存取
	if request.method == 'POST':
		id=request.POST["id"]
		if id.strip()=="999":
			return redirect("/rank/")
		try: #如果get不到的例外處理
			country=Country.objects.get(id=id)
		except:
			return redirect("/rank/")
		cities =City.objects.filter(country=country).order_by('population')
	else:
		cities=City.objects.all().order_by('population') #.order_by('population') 依照人口population進行排序
	countries=Country.objects.all()
	return render(request, "rank.html", locals())

@login_required(login_url="/admin/login/")
def chart(request):
	#cities=City.objects.all()
	if request.method == 'POST':
		id=request.POST["id"]
		if id.strip()=="999":
			return redirect("/chart/")
		try: #如果get不到的例外處理
			country=Country.objects.get(id=id)
		except:
			return redirect("/chart/")
		cities =City.objects.filter(country=country) 
	else:
		cities=City.objects.all() #.order_by('population') 依照人口population進行排序
	countries=Country.objects.all()
	name=[city.name for city in cities ]
	population=[city.population for city in cities]
	return render(request, "chart.html", locals())


def mylogout(request):
	logout(request)
	return redirect("/")

def delete(request,id):
	try:
		post=Post.objects.get(id=id)
		post.delete()
	except:
		return redirect("/news/")
	return redirect("/news/")

def deletenote(request,id):
	try:
		note=Note.objects.get(id=id)
		note.delete()
	except:
		return redirect("/note/")
	return redirect("/note/")

def addnote(request):
	if request.method=="POST":
		title=request.POST["title"]
		if len(title) > 10:
			note=Note(title=title)
			note.save()
	return redirect("/note/")

def note(request):
	notes=Note.objects.all()
	return render(request, "note.html", locals())




#下一步到templates內產生xxxx.html檔案(可以複製相同的html檔案 過去更改檔名)