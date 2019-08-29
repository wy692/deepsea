from django.shortcuts import render_to_response
from .models import Microrna
# Create your views here.
def microrna(request):
	context={}
	context['micrornas'] = Microrna.objects.all()
	return render_to_response('microrna/microrna.html',context)