
from django.urls import path
from .views import inicio, otra_vista, numero_random, numero_del_usuario, mi_plantilla, login, registrar, editar
from django.contrib.auth.views import   LogoutView   
  
urlpatterns = [   
    path('', inicio, name="inicio"),
    path('otra-vista', otra_vista, name="otra_vista"),
    path('numero-random/', numero_random, name="numero_random"),
    path('dame-numero/<int:numero>', numero_del_usuario, name="numero_del_usuario"), #A esto me referia en views, ademas agrego INT para que sepa que es num
    path('mi-plantilla', mi_plantilla, name="mi_plantilla"),
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('editar/', editar, name='editar'),
    path('logout/', LogoutView.as_view(template_name='indice/index.html'), name='logout') 
]