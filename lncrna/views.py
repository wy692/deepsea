from django.shortcuts import render_to_response
from .models import Lncrna
# Create your views here.
def lncrna(request):
	context={}
	context['lncrnas'] = Lncrna.objects.all()
	return render_to_response('lncrna/lncrna.html',context)