from django.shortcuts import render
from .forms import DecodeForm, EncodeForm
from django.core.files.storage import FileSystemStorage
from .stegano import decode, encode
from Project.settings import BASE_DIR
from django.http import FileResponse
from django.utils.safestring import mark_safe

import os
import urllib.parse



def home(request):
    return render(request, 'index.html')

def encoder_view(request):
    return render(request, 'encode.html')


def img_encode(request):
    if request.method == "POST":
        form = EncodeForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            img_name = mark_safe(image.name)
            quoted_img_name = urllib.parse.quote(img_name)
            filename = fs.save(quoted_img_name, image)
           
            # encode the text
            

            img = os.path.join(os.path.dirname(BASE_DIR), 'assets', quoted_img_name)
            new_img_name = quoted_img_name.split(".")[0] + '_encoded.' + quoted_img_name.split(".")[-1]
            new_img = os.path.join(os.path.dirname(BASE_DIR), 'assets', new_img_name)
            
            encode(img, text, new_img)
            file_path = new_img
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=new_img_name)

        else:
            print(form.errors)

    return render(request, 'encode.html')



def decoder_view(request):
    return render(request, 'decode.html')


def img_decode(request):
    if request.method == "POST":
        form = DecodeForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            img_name = mark_safe(image.name)
            quoted_img_name = urllib.parse.quote(img_name)

            fs = FileSystemStorage()
            filename = fs.save(quoted_img_name, image)
           
            # decode the image
            img = os.path.join(os.path.dirname(BASE_DIR), 'assets', quoted_img_name)
            decoded_text = decode(img)

            return render(request, "decode.html", {'decoded_msg': mark_safe(decoded_text)})
        else:
            print(form.errors)

    return render(request, 'decode.html')
