from django.shortcuts import render, HttpResponse

html_base ="""
<h1>Mi web personal </h1>
<ul>
    <li><a href ="/">Portada</a></li>
    <li><a href ="/about/">Acerca de</a></li>
    <li><a href ="/portfolio/">Portafolio</a></li>
    <li><a href ="/contact/">Contacto</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base+"""
    <h2>Portada</h2>
    <p> Esto es la portada</p>
    """)

def about(request):
    return HttpResponse("<h1> Acerca de </h1><h2>Portada</h2>")

def portfolio(request):
    return HttpResponse("<h1>Portafolio</h1>")

def contact(request):
    return HttpResponse("<h1>Contacto</h1>")
