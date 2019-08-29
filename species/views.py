from django.shortcuts import render_to_response
from .models import Species

# Create your views here.

def species(request):
	context = {}
	context['species'] = Species.objects.all()
	return render_to_response('species/species_list.html',context)
	
