from django.shortcuts import render_to_response
from .models import Circrna
# Create your views here.
def circrna(request):
	context={}
	context['circrnas'] = Circrna.objects.all()
	return render_to_response('circrna/circrna.html',context)