# Create your views here.
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import Http404, HttpResponse

def main(request):
    t=get_template('base.html')
    html= t.render(Context({'title':'BSC GPA'}))
    return HttpResponse(html)

def mision(request):
    t=get_template('mision.html')
    html= t.render(Context({'title':'BSC GPA'}))
    return HttpResponse(html)    

def perspectiva(request):
    t=get_template('perspectiva.html')
    html= t.render(Context({'title':'BSC GPA', 'empresa':'Gobierno Provincial del Azuay'}))
    return HttpResponse(html)    