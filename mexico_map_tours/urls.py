"""mexico_map_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from estados import views

app_name = 'estadosurl'

urlpatterns = [
    path('calacaadminsupersecreto', admin.site.urls),
    path('acerca', views.about, name='about'),
    path('', views.index, name='index'),
    path('privacidad', views.privacidad, name='privacidad'),
    path('aguascalientes', views.aguascalientes, name='aguascalientes'),
    path('baja_california', views.baja_california, name='baja_california'),
    path('baja_california_sur', views.baja_california_sur, name='baja_california_sur'),
    path('campeche', views.campeche, name='campeche'),
    path('chiapas', views.chiapas, name='chiapas'),
    path('chihuahua', views.chihuahua, name='chihuahua'),
    path('coahuila', views.coahuila, name='coahuila'),
    path('colima', views.colima, name='colima'),
    path('ciudad_de_mexico', views.ciudad_de_mexico, name='ciudad_de_mexico'),
    path('durango', views.durango, name='durango'),
    path('guanajuato', views.guanajuato, name='guanajuato'),
    path('guerrero', views.guerrero, name='guerrero'),
    path('hidalgo', views.hidalgo, name='hidalgo'),
    path('jalisco', views.jalisco, name='jalisco'),
    path('estado_de_mexico', views.estado_de_mexico, name='estado_de_mexico'),
    path('michoacan', views.michoacan, name='michoacan'),
    path('morelos', views.morelos, name='morelos'),
    path('nayarit', views.nayarit, name='nayarit'),
    path('nuevo_leon', views.nuevo_leon, name='nuevo_leon'),
    path('oaxaca', views.oaxaca, name='oaxaca'),
    path('puebla', views.puebla, name='puebla'),
    path('queretaro', views.queretaro, name='queretaro'),
    path('quintana_roo', views.quintana_roo, name='quintana_roo'),
    path('san_luis_potosi', views.san_luis_potosi, name='san_luis_potosi'),
    path('sinaloa', views.sinaloa, name='sinaloa'),
    path('sonora', views.sonora, name='sonora'),
    path('tabasco', views.tabasco, name='tabasco'),
    path('tamaulipas', views.tamaulipas, name='tamaulipas'),
    path('tamaulipas/<int:video_id>/', views.tamaulipas_video, name="tamaulipas_video"),
    path('tlaxcala', views.tlaxcala, name='tlaxcala'),
    path('veracruz', views.veracruz, name='veracruz'),
    path('yucatan', views.yucatan, name='yucatan'),
    path('zacatecas', views.zacatecas, name='zacatecas'),

]
