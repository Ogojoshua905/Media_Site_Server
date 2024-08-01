from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings # or from my_app.settings Import MEDIA_ROOT
import json
import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def css(request):
    return render(request, 'styles.css')

def home(request):
    return HttpResponse("<body style='background-color: black; color: white;'><nav style=''><span></span></nav><h1 style='color: red; text-align: center; padding: 15px 32px; text-decoration: underline;'>My Data to You</h1><br><h2>Name: <span style='color: red;'>Byte</span><span style='color: purple;'>Prowler</span></h2><br> <h2>Occupation: <span style='color:pink;'>Code Bomber</span></h2></body>,", content_type="text/html", status=200)

def message(request, word): # Parameter
    return HttpResponse(f"{word}", content_type="text/html") #or text/plain

def download_pdf(request):
    pdf_path = os.path.join("media", "tsotb.pdf")

    # open file in binary mode. rb means read binary
    with open(pdf_path,'rb') as pdf_file:
        pdf_content = pdf_file.read()
    # create a http response with pdf content
    response = HttpResponse(pdf_content, content_type="application/pdf", status=200)
    # response['Content-Disposition'] = 'attachment; filename="tsotb.pdf"'
    return response