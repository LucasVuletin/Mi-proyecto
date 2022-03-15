
from django.urls import path
from .views import inicio, otra_vista, numero_random, numero_del_usuario, mi_plantilla   
  
urlpatterns = [   
    path('inicio/', inicio),
    path('', otra_vista),
    path('numero-random/', numero_random),
    path('dame-numero/<int:numero>', numero_del_usuario), #A esto me referia en views, ademas agrego INT para que sepa que es num
    path('mi-plantilla', mi_plantilla), 
]