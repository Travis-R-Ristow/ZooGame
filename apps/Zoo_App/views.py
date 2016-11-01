from django.shortcuts import render, redirect
from django.contrib import messages
# from .models import User
import random
# import re
# Create your views here.
def index(request):
	if 'money' not in request.session:
		request.session['money'] = 0
	if 'highscore' not in request.session:
		request.session['highscore']=60420

	if 'day' not in request.session:
		request.session['day'] = 16
	if 'tickets' not in request.session:
		request.session['tickets'] = 1

	if 'randStart' not in request.session:
		request.session['randStart'] = 5
	if 'randEnd' not in request.session:
		request.session['randEnd'] = 10
	if 'workers' not in request.session:
		request.session['workers'] = 1

	if 'dolph' not in request.session:
		request.session['dolph'] = 0
	if 'dolphCOST' not in request.session:
		request.session['dolphCOST'] = 10
	if 'dolphWORK' not in request.session:
		request.session['dolphWORK'] = 2

	if 'polar' not in request.session:
		request.session['polar'] = 0
	if 'polarCOST' not in request.session:
		request.session['polarCOST'] = 30
	if 'polarWORK' not in request.session:
		request.session['polarWORK'] = 3

	if 'gorilla' not in request.session:
		request.session['gorilla'] = 0
	if 'gorillaCOST' not in request.session:
		request.session['gorillaCOST'] = 20
	if 'gorillaWORK' not in request.session:
		request.session['gorillaWORK'] = 4

	if 'dino' not in request.session:
		request.session['dino'] = 0
	if 'dinoCOST' not in request.session:
		request.session['dinoCOST'] = 50
	if 'dinoWORK' not in request.session:
		request.session['dinoWORK'] = 6

	if 'ach1' not in request.session:
		request.session['ach1'] = True
	if 'ach2' not in request.session:
		request.session['ach2'] = True
	if 'ach3' not in request.session:
		request.session['ach3'] = True
	if 'ach4' not in request.session:
		request.session['ach4'] = True

	if request.session['dolph'] > 4 and request.session['ach1'] == True:
		request.session['info'] = 'Achievement 1 of 8: +1 Days'
		request.session['day'] += 1
		request.session['ach1'] = False
	if request.session['polar'] > 4 and request.session['ach2'] == True:
		request.session['info'] = 'Achievement 2 of 8: +1 Days'
		request.session['day'] += 1
		request.session['ach2'] = False
	if request.session['gorilla'] > 4 and request.session['ach3'] == True:
		request.session['info'] = 'Achievement 3 of 8: +1 Days'
		request.session['day'] += 1
		request.session['ach3'] = False
	if request.session['dino'] > 4 and request.session['ach4'] == True:
		request.session['info'] = 'Achievement 4 of 8: +1 Days'
		request.session['day'] += 1
		request.session['ach4'] = False
	request.session['score'] = (request.session['dolph']*10)+(request.session['polar']*30)+(request.session['gorilla']*20)+(request.session['dino']*50)+(request.session['money'])
	request.session['avg'] = ((request.session['randStart']-request.session['tickets']) + (request.session['randEnd']-request.session['tickets'])) /2
	return render(request, 'Zoo_App/index.html')

def reset(request):
	del request.session['money']
	del request.session['day']
	del request.session['randStart']
	del request.session['randEnd']
	del request.session['workers']
	del request.session['tickets']
	del request.session['dolph']
	del request.session['dolphCOST']
	del request.session['dolphWORK']
	del request.session['polar']
	del request.session['polarCOST']
	del request.session['polarWORK']
	del request.session['gorilla']
	del request.session['gorillaCOST']
	del request.session['gorillaWORK']
	del request.session['dino']
	del request.session['dinoCOST']
	del request.session['dinoWORK']
	del request.session['info']
	del request.session['ach1']
	del request.session['ach2']
	del request.session['ach3']
	del request.session['ach4']
	return redirect('/')
def HRDreset(request):
	request.session.clear()
	return redirect('/')

#####################################################
				##TICKETS##

def ticInc(request):
	request.session['tickets'] += 1
	return redirect('/')

def ticDec(request):
	request.session['tickets'] -= 1
	if request.session['tickets'] < 0:
		request.session['tickets'] = 0
	return redirect('/')

#####################################################
				##CLICKS##

def click(request):
	if ((request.session['dolph']*2) or (request.session['polar']*3) or (request.session['gorilla']*4) or (request.session['dino']*6)) < request.session['workers']+1:
		request.session['customers'] = random.randrange(request.session['randStart']-request.session['tickets'], request.session['randEnd']-request.session['tickets'])
		if request.session['customers'] < 0:
			request.session['customers'] = 0

		request.session['info'] = "{} People Bought Tickets".format(request.session['customers'])
		request.session['day'] -= 1
		request.session['money'] += (request.session['customers']*request.session['tickets'])
		request.session['money'] -= request.session['workers']*3

		if request.session['day'] < 1:
			if request.session['highscore'] < request.session['score']:
				request.session['highscore'] = request.session['score']
			return redirect('/reset')
		else:
			return redirect('/')
	else:
		request.session['info'] = 'Not Enough Workers'
		return redirect('/')


#####################################################
				##WORKERS##
def addWorkers(request):
	request.session['workers'] += 1
	return redirect('/')

def subWorkers(request):
	request.session['workers'] -= 1
	if request.session['workers'] < 1:
		request.session['workers'] = 1
	return redirect('/')

#####################################################
				##ANIMALS##
def dolph(request):
	if request.session['workers'] < request.session['dolphWORK']:
		request.session['info'] = 'You need more Workers.'
		return redirect('/')
	if request.session['money'] < request.session['dolphCOST']:
		request.session['info'] = 'You need more Money.'
		return redirect('/')
	else:
		request.session['dolph'] += 1
		request.session['dolphWORK'] += 2
		request.session['money'] -= request.session['dolphCOST']
		# request.session['dolphCOST'] += 10
		request.session['info'] = 'Dolphin Bought'
		request.session['randStart'] += 1
		request.session['randEnd'] += 1
		return redirect('/')

def polarBear(request):
	if request.session['workers'] < request.session['polarWORK']:
		request.session['info'] = 'You need more Workers.'
		return redirect('/')
	if request.session['money'] < request.session['polarCOST']:
		request.session['info'] = 'You need more Money.'
		return redirect('/')
	else:
		request.session['polar'] += 1
		request.session['polarWORK'] += 3
		request.session['money'] -= request.session['polarCOST']
		# request.session['polarCOST'] += 30
		request.session['info'] = 'Polar Bear Bought'
		request.session['randStart'] += 2
		request.session['randEnd'] += 2
		return redirect('/')

def gorilla(request):
	if request.session['workers'] < request.session['gorillaWORK']:
		request.session['info'] = 'You need more Workers.'
		return redirect('/')
	if request.session['money'] < request.session['gorillaCOST']:
		request.session['info'] = 'You need more Money.'
		return redirect('/')
	else:
		request.session['gorilla'] += 1
		request.session['gorillaWORK'] += 4
		request.session['money'] -= request.session['gorillaCOST']
		# request.session['gorillaCOST'] += 20
		request.session['info'] = 'Gorilla Bought'
		request.session['randStart'] += 2
		request.session['randEnd'] += 2
		return redirect('/')

def dino(request):
	if request.session['workers'] < request.session['dinoWORK']:
		request.session['info'] = 'You need more Workers.'
		return redirect('/')
	if request.session['money'] < request.session['dinoCOST']:
		request.session['info'] = 'You need more Money.'
		return redirect('/')
	else:
		request.session['dino'] += 1
		request.session['dinoWORK'] += 6
		request.session['money'] -= request.session['dinoCOST']
		# request.session['dinoCOST'] += 50
		request.session['info'] = 'Dinosaur Bought'
		request.session['randStart'] += 5
		request.session['randEnd'] += 5
		return redirect('/')