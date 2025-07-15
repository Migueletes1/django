"""from django.shortcuts import render
from django.http import HttpResponse


def members(request):
    return HttpResponse("Hello, world. You're at the members page.")"""

from django.http import HttpResponse
from django.template import loader


def members(request):
    template = loader.get_template("mi_app/myfirst.html")
    return HttpResponse(template.render())
