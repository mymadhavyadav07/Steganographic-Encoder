from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('encoder', views.encoder_view, name='encoder_view'),
    path('encoder/encode', views.img_encode, name='encode'),
    
    path('decoder', views.decoder_view, name='decoder_view'),
    path('decoder/decode', views.img_decode, name='decode'),
    
    
]
