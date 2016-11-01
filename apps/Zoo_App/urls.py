from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^click$', views.click),
	url(r'^reset$', views.reset),
	url(r'^ticInc$', views.ticInc),
	url(r'^ticDec$', views.ticDec),
	url(r'^addWorkers$', views.addWorkers),
	url(r'^subWorkers$', views.subWorkers),
	url(r'^dolph$', views.dolph),
	url(r'^polarBear$', views.polarBear),
	url(r'^gorilla$', views.gorilla),
	url(r'^dino$', views.dino),
	url(r'^HRDreset$', views.HRDreset),
]