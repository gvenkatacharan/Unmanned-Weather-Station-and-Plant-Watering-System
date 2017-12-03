# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Temperature,Humidity,Plant,Waterlevel,Watersensor,Plantcondition #importing the models
from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse

def check(request):
	if request.method == 'POST':
		username = request.POST['uname']
		password = request.POST['password']
		if(username == 'group25' and password =='password1234'):
			return redirect('/index')
	return render(request,'plants/login.html')
	
def addplant(request):
	if request.method == 'POST':
		m_obj=Plant()
		m_obj.plant_id=request.POST['plantid']
		m_obj.latitude=request.POST['lat']
		m_obj.longitude=request.POST['long']
		m_obj.save()
	return redirect('/index')

def index(request):
	temp_data=Temperature.objects.all()[len(Temperature.objects.all())-1] #retrieving the last stored value of the temperature from the database
	temp_data=str(temp_data)
	hum_data=Humidity.objects.all()[len(Humidity.objects.all())-1] #retrieving the last stored value of the humdity from the database
	hum_data=str(hum_data)
	t=len(Plant.objects.all())
	latitude=[]
	longitude=[]
	for i in range(t,0,-1):
		x=Plant.objects.all()[len(Plant.objects.all())-(i)]
		latitude.append(float(x.latitude))
		longitude.append(float(x.longitude))

	x=Plant.objects.all()[len(Plant.objects.all())-(t)]	#retrieving the last stored value of the soil maoisture of a particular plant from the database
	y=x.plantcondition_set.all()[len(x.plantcondition_set.all())-1]
	if int(x.plant_id)==1:
		p1_moi=float(y.moi_value)
	else:
		p2_moi=float(y.moi_value)
	x=Plant.objects.all()[len(Plant.objects.all())-(t-1)]
	y=x.plantcondition_set.all()[len(x.plantcondition_set.all())-1]
	if int(x.plant_id)==1:
		p1_moi=float(y.moi_value)
	else:
		p2_moi=y.moi_value	

	water_data=Waterlevel.objects.all()[len(Waterlevel.objects.all())-1]	#retrieving the last stored value of the waterlevel from the database
	water_data=str(water_data)
	water_sensor=Watersensor.objects.all()[len(Watersensor.objects.all())-1]	#retrieving the last stored value of the watersensor values from the database
	water_sensor=str(water_sensor)
	x1=[]
	x2=[]
	x31=[]
	x32=[]
	for i in range(0,10):
	    t1=Temperature.objects.all()[len(Temperature.objects.all())-(10-i)]	#retrieving the prevoius 10 values of the temperature that are in the database for the purpose of graph
	    t1=str(t1)
	    t1=float(t1)
	    x1.append(t1)
	    t2=Humidity.objects.all()[len(Humidity.objects.all())-(10-i)]	#retrieving the prevoius 10 values of the humidity that are in the database for the purpose of graph
	    t2=str(t2)
	    t2=float(t2)
	    x2.append(t2)
															
			#retrieving the prevoius 10 values of the soilmoisture that are in the database for the purpose of graph	
	x=Plant.objects.all()[len(Plant.objects.all())-(t)]
	for i in range(0,10):
		y=x.plantcondition_set.all()[len(x.plantcondition_set.all())-(10-i)]	
		x31.append(float(y.moi_value))
	x=Plant.objects.all()[len(Plant.objects.all())-(t-1)]
	for i in range(0,10):
		y=x.plantcondition_set.all()[len(x.plantcondition_set.all())-(10-i)]	
		x32.append(float(y.moi_value))

	context={'sensor1':temp_data,'sensor2':hum_data,'sensor3':p1_moi,'sensor4':water_data,'sensor5':water_sensor,'sensor6':p2_moi,'graph1':x1,'graph2':x2,'graph3':x31,'graph4':x32,'n':t,'latitude':latitude,'longitude':longitude}
	return render(request,'plants/index.html',context)	#sending all the values to the webpage 
def getdata(request):
	if request.method=='GET' :
		temp_value=request.GET['temperature']  
		t_obj=Temperature()
		t_obj.tem_value=temp_value					#storing the temperature sensor values in the database which are just arrived from the pi based on the key word 'temperatuer'
		t_obj.save()
		hum_value=request.GET['humidity']
		h_obj=Humidity()
		h_obj.hum_value=hum_value					#storing the humidity sensor values in the database which are just arrived from the pi based on the key word 'humidity'
		h_obj.save()
		plant_id=request.GET['id']
		moi_value=request.GET['moisture']
		actuator_value=request.GET['actuator']			#storing the plant id and their corresponding soilmoisture values in the database 
		plant_obj=Plant.objects.get(plant_id=plant_id)
		plant_obj.plantcondition_set.create(moi_value=moi_value,actuator_value=actuator_value)
		water_value=request.GET['waterlevel']		#storing the waterlevel values in the database which are just arrived from the pi based on the key word 'waterlevel'
		w_obj=Waterlevel()
		w_obj.water_value=water_value
		w_obj.save()
		water_sensor=request.GET['watersensor']		#storing the watersensor values in the database which are just arrived from the pi based on the key word 'watersensor'
		w_obj=Watersensor()
		w_obj.water_sensor=water_sensor		
		w_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")
