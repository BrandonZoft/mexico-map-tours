from django.shortcuts import render, get_object_or_404
import json 
from .models import *
import django_filters
from django.core.paginator import Paginator

# coat of arms from wikimedia
cc_aguascalientes = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Coat_of_arms_of_Aguascalientes.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Aguascalientes.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Aguascalientes (México)"
}

cc_bajacalifornia = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Coat_of_arms_of_Baja_California.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Baja_California.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de la Baja California (México)"
}

cc_bajacaliforniasur = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Coat_of_Arms_of_Baja_California_Sur.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_Arms_of_Baja_California_Sur.svg",
    "author": "Heralder Elements por Sodacan",
    "author_url": "https://commons.wikimedia.org/wiki/User:Sodacan",
    "title": "Escudo del Estado de la Baja California Sur (México)"
}

cc_chiapas = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Coat_of_arms_of_Chiapas.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Chiapas.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Chiapas (México)"
}

cc_campeche = {
    "license": "CC BY 3.0",
    "license_url": "https://creativecommons.org/licenses/by/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Coat_of_arms_of_Campeche.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Campeche.svg",
    "author": "El Ágora",
    "author_url": "https://commons.wikimedia.org/wiki/User:El_%C3%81gora",
    "title": "Escudo del Estado de Campeche (México)"
}

cc_chihuahua = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/42/Escudo_de_Armas_de_la_Ciudad_de_Chihuahua.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Escudo_de_Armas_de_la_Ciudad_de_Chihuahua.svg",
    "author": "Danielmm88",
    "author_url": "https://commons.wikimedia.org/wiki/User:Danielmm88",
    "title": "Escudo del Estado de Campeche (México)"
}

cc_coahuila = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Coat_of_arms_of_Coahuila.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Coahuila.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Coahuila (México)"
}

cc_colima = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Coat_of_arms_of_Colima.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Colima.svg",
    "author": "Yavidaxiu",
    "author_url": "https://commons.wikimedia.org/wiki/User:Yavidaxiu",
    "title": "Escudo del Estado de Colima (México)"
}

cc_durango = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Coat_of_arms_of_Durango.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Durango.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Durango (México)"
}

cc_jalisco = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Escudo_de_Armas_de_Guadalajara_%28Jalisco%29.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Escudo_de_Armas_de_Guadalajara_(Jalisco).svg",
    "author": "Jpablo_cad",
    "author_url": "https://guadalajara.gob.mx/",
    "title": "Escudo del Estado de Jalisco (México)"
}

cc_guanajuato = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Coat_of_arms_of_Guanajuato.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Guanajuato.svg",
    "author": "Giggette",
    "author_url": "https://commons.wikimedia.org/wiki/User:Giggette",
    "title": "Escudo del Estado de Guanajuato (México)"
}

cc_guerrero = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Coat_of_arms_of_Guerrero.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Guerrero.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Guerrero (México)"
}

cc_hidalgo = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/df/Coat_of_arms_of_Hidalgo.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Hidalgo.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Hidalgo (México)"
}

cc_mexicocity = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/archive/2/21/20200523223230%21Coat_of_arms_of_Mexico_City%2C_Mexico.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Mexico_City,_Mexico.svg",
    "author": "VegaMex",
    "author_url": "https://congresocdmx.gob.mx/archivos/parlamentarios/IN_298_11_20_02_2020.pdf",
    "title": "Escudo de la ciudad de México (México)"
}

cc_michoacan = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Coat_of_arms_of_Michoacan.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Michoacan.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Michoacan (México)"
}

cc_morelos = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/0/01/Coat_of_arms_of_Morelos.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Morelos.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Morelos (México)"
}

cc_nayarit = {
    "license": "Dominio Publico",
    "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Coat_of_arms_of_Nayarit.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Nayarit.svg",
    "author": "Heraldicos",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldicos",
    "title": "Escudo del Estado de Nayarit (México)"
}

cc_nuevoleon = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Coat_of_arms_of_Nuevo_Leon.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Nuevo_Leon.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Nuevo León (México)"
}

cc_oaxaca = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/2a/Coat_of_arms_of_Oaxaca.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Oaxaca.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del Estado de Oaxaca (México)"
}

cc_puebla = {
    "license": "CC BY-SA 4.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Coat_of_arms_of_Puebla.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Puebla.svg",
    "author": "Yavidaxiu",
    "author_url": "https://commons.wikimedia.org/wiki/User:Yavidaxiu",
    "title": "Escudo del Estado de Puebla (México)"
}

cc_queretaro = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Coat_of_arms_of_Queretaro.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Queretaro.svg",
    "author": "Yavidaxiu",
    "author_url": "https://commons.wikimedia.org/wiki/User:Yavidaxiu",
    "title": "Escudo del estado de Querétaro Arteaga (México)"
}

cc_quintana = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/7/77/Coat_of_arms_of_Quintana_Roo.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Quintana_Roo.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del estado de Quintana Roo (México)"
}

cc_sanluispotosi = {
    "license": "CC BY-SA 4.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Coat_of_arms_of_San_Luis_Potosi.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_San_Luis_Potosi.svg",
    "author": "Yavidaxiu",
    "author_url": "https://commons.wikimedia.org/wiki/User:Yavidaxiu",
    "title": "Escudo del estado de San Luis Potosí (México)"
}

cc_sinaloa = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Coat_of_arms_of_Sinaloa.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Sinaloa.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del estado de Sinaloa (México)"
}

cc_sonora = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Coat_of_arms_of_Sonora.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Sonora.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del estado de Sonora (México)"
}

cc_tabasco = {
    "license": "CC BY-SA 4.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b0/Coat_of_arms_of_Tabasco_%28M%C3%A9xico%29.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Tabasco_(M%C3%A9xico).svg",
    "author": "Konstantinopoulosstephanopoulos",
    "author_url": "https://commons.wikimedia.org/wiki/User:Konstantinopoulosstephanopoulos",
    "title": "Escudo del estado de Tabasco (México)"
}

cc_tamaulipas = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/90/Coat_of_arms_of_Tamaulipas.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Tamaulipas.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del estado de Tamaulipas (México)"
}

cc_tlaxcala = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/18/Coat_of_arms_of_Tlaxcala.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Tlaxcala.svg",
    "author": "Battroid",
    "author_url": "https://commons.wikimedia.org/wiki/User:Battroid",
    "title": "Escudo del estado de Tlaxcala (México)"
}

cc_veracruz = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/84/Coat_of_arms_of_Veracruz.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Veracruz.svg",
    "author": "Heraldry",
    "author_url": "https://commons.wikimedia.org/wiki/User:Heraldry",
    "title": "Escudo del estado de Veracruz (México)"
}

cc_zacatecas = {
    "license": "CC BY-SA 4.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/4.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Escudo_de_armas_de_la_Ciudad_y_Estado_de_Zacatecas.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Escudo_de_armas_de_la_Ciudad_y_Estado_de_Zacatecas.svg",
    "author": "VegaMex",
    "author_url": "https://commons.wikimedia.org/wiki/User:VegaMex",
    "title": "Escudo del estado de Zacatecas (México)"
}

cc_estadomexico = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/archive/5/5b/20200525154405%21Coat_of_arms_of_Mexico_State.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Mexico_State.svg",
    "author": "Sofree",
    "author_url": "http://portal2.edomex.gob.mx/edomex/estado/simbolos/EDOMEX_024337",
    "title": "Escudo del estado de Mexico (México)"
}

cc_yucatan = {
    "license": "CC BY-SA 3.0",
    "license_url": "https://creativecommons.org/licenses/by-sa/3.0/deed.en",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/5/54/Coat_of_arms_of_Yucatan.svg",
    "image_license_url": "https://commons.wikimedia.org/wiki/File:Coat_of_arms_of_Yucatan.svg",
    "author": "TownDown",
    "author_url": "https://commons.wikimedia.org/wiki/User:TownDown",
    "title": "Escudo del estado de Yucatán (México)"
}





def index(request):
    return render(request,'estados/index.html')

def privacidad(request):
    return render(request,'estados/privacy.html')

def about(request):
    return render(request,'estados/about.html')

def aguascalientes(request):
    estado = Aguascalientes.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'aguascalientes_video', 'name': "Aguascalientes", "statecoat": cc_aguascalientes})

def baja_california(request):
    estado = BajaCalifornia.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'baja_california_video', 'name': "Baja California", "statecoat": cc_bajacalifornia})

def baja_california_sur(request):
    estado = BajaCaliforniaSur.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'baja_california_sur_video', 'name': "Baja California Sur", "statecoat": cc_bajacaliforniasur})

def campeche(request):
    estado = Campeche.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'campeche_video', 'name': "Campeche", "statecoat": cc_campeche})

def chiapas(request):
    estado = Chiapas.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'chiapas_video', 'name': "Chiapas", "statecoat": cc_chiapas})

def chihuahua(request):
    estado = Chihuahua.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'chihuahua_video', 'name': "Chihuahua", "statecoat": cc_chihuahua})

def coahuila(request):
    estado = Coahuila.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'coahuila_video', 'name': "Coahuila", "statecoat": cc_coahuila})

def colima(request):
    estado = Colima.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'colima_video', 'name': "Colima", "statecoat": cc_colima})

def ciudad_de_mexico(request):
    estado = CiudadDeMexico.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'ciudad_de_mexico_video', 'name': "Ciudad de México", "statecoat": cc_mexicocity})

def durango(request):
    estado = Durango.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'durango_video', 'name': "Durango", "statecoat": cc_durango})

def guanajuato(request):
    estado = Guanajuato.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'guanajuato_video', 'name': "Guanajuato", "statecoat": cc_guanajuato})

def guerrero(request):
    estado = Guerrero.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'guerrero_video', 'name': "Guerrero", "statecoat": cc_guerrero})

def hidalgo(request):
    estado = Hidalgo.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'hidalgo_video', 'name': "Hidalgo", "statecoat": cc_hidalgo})

def jalisco(request):
    estado = Jalisco.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'jalisco_video', 'name': "Jalisco", "statecoat": cc_jalisco})

def estado_de_mexico(request):
    estado = EstadoDeMexico.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'estado_de_mexico_video', 'name': "Estado de México", "statecoat": cc_estadomexico})

def michoacan(request):
    estado = Michoacan.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'michoacan_video', 'name': "Michoacán", "statecoat": cc_michoacan})

def morelos(request):
    estado = Morelos.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'morelos_video', 'name': "Morelos", "statecoat": cc_morelos})

def nayarit(request):
    estado = Nayarit.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'nayarit_video', 'name': "Nayarit", "statecoat": cc_nayarit})

def nuevo_leon(request):
    estado = NuevoLeon.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'nuevo_leon_video', 'name': "Nuevo León", "statecoat": cc_nuevoleon})

def oaxaca(request):
    estado = Oaxaca.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'oaxaca_video', 'name': "Oaxaca", "statecoat": cc_oaxaca})

def puebla(request):
    estado = Puebla.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'puebla_video', 'name': "Puebla", "statecoat": cc_puebla})

def queretaro(request):
    estado = Queretaro.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'queretaro_video', 'name': "Querétaro", "statecoat": cc_queretaro})

def quintana_roo(request):
    estado = QuintanaRoo.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'quintana_roo_video', 'name': "Quintana Roo", "statecoat": cc_quintana})

def san_luis_potosi(request):
    estado = SanLuisPotosi.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'san_luis_potosi_video', 'name': "San Luis Potosí", "statecoat": cc_sanluispotosi})

def sinaloa(request):
    estado = Sinaloa.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'sinaloa_video', 'name': "Sinaloa", "statecoat": cc_sinaloa})

def sonora(request):
    estado = Sonora.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'sonora_video', 'name': "Sonora", "statecoat": cc_sonora})

def tabasco(request):
    estado = Tabasco.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'tabasco_video', 'name': "Tabasco", "statecoat": cc_tabasco})

def tamaulipas(request):
    estado = Tamaulipas.objects.all()
        
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'tamaulipas_video', 'name': "Tamaulipas", "statecoat": cc_tamaulipas})

def tamaulipas_video(request, video_id):
    video = get_object_or_404(Tamaulipas, pk=video_id)
    return render(request, 'estados/video.html', {'video':video})

def tlaxcala(request):
    estado = Tlaxcala.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'tlaxcala_video', 'name': "Tlaxcala", "statecoat": cc_tlaxcala})

def veracruz(request):
    estado = Veracruz.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'veracruz_video', 'name': "Veracruz", "statecoat": cc_veracruz})

def yucatan(request, estado_id):
    estado = Yucatán.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'yucatan_video', 'name': "Yucatán", "statecoat": cc_yucatan})

def zacatecas(request):
    estado = Zacatecas.objects.all()
    estado_paginator = Paginator(estado, 15)

    page_num = request.GET.get('page')
    page = estado_paginator.get_page(page_num)
    return render(request,'estados/estado.html', {'estado':page, 'estado_url': 'zacatecas_video', 'name': "Zacatecas", "statecoat": cc_zacatecas})

# flags from: https://commons.wikimedia.org/wiki/File:Flag_of_Aguascalientes.svg
# flag_aguascalientes = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Aguascalientes.svg"
# flag_bajacalifornia = "https://upload.wikimedia.org/wikipedia/commons/2/27/Flag_of_Baja_California.svg"
# flag_bajacaliforniasur = "https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Baja_California_Sur.svg"
# flag_campeche = "https://upload.wikimedia.org/wikipedia/commons/3/37/Flag_of_Campeche.svg"
# flag_chiapas = "https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Chiapas.svg"
# flag_chihuahua = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Chihuahua.svg"
# flag_coahuila = "https://upload.wikimedia.org/wikipedia/commons/d/d2/Flag_of_Coahuila.svg"
# flag_colima = "https://upload.wikimedia.org/wikipedia/commons/5/52/Flag_of_Colima.svg"
# flag_ciudadmex = "https://upload.wikimedia.org/wikipedia/commons/b/b3/Flag_of_Mexico_City%2C_Mexico.svg"
# flag_durango = "https://upload.wikimedia.org/wikipedia/commons/7/70/Flag_of_Durango.svg"
# flag_guanajuato = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Flag_of_Guanajuato.svg"
# flag_guerrero = "https://upload.wikimedia.org/wikipedia/commons/b/b8/Flag_of_Guerrero.svg"
# flag_hidalgo = "https://upload.wikimedia.org/wikipedia/commons/0/0d/Flag_of_Hidalgo.svg"
# flag_jalisco = "https://upload.wikimedia.org/wikipedia/commons/2/2b/Flag_of_Jalisco.svg"
# flag_estadomex = "https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_the_State_of_Mexico.svg"
# flag_michoacan = "https://upload.wikimedia.org/wikipedia/commons/0/02/Flag_of_Michoacan.svg"
# flag_morelos = "https://upload.wikimedia.org/wikipedia/commons/f/fd/Flag_of_Morelos.svg"
# flag_nayarit = "https://upload.wikimedia.org/wikipedia/commons/a/ac/Flag_of_Nayarit.svg"
# flag_nuevoleon = "https://upload.wikimedia.org/wikipedia/commons/8/80/Flag_of_Nuevo_Leon.svg"
# flag_oaxaca = "https://upload.wikimedia.org/wikipedia/commons/b/b2/Flag_of_Oaxaca.svg"
# flag_puebla = "https://upload.wikimedia.org/wikipedia/commons/c/cd/Flag_of_Puebla.svg"
# flag_queretaro = "https://upload.wikimedia.org/wikipedia/commons/1/18/Flag_of_Queretaro.svg"
# flag_quintana = "https://upload.wikimedia.org/wikipedia/commons/a/a0/Flag_of_Quintana_Roo.svg"
# flag_sanluis = "https://upload.wikimedia.org/wikipedia/commons/9/99/Flag_of_San_Luis_Potosi.svg"
# flag_sinaloa = "https://upload.wikimedia.org/wikipedia/commons/c/cc/Flag_of_Sinaloa.svg"
# flag_sonora = "https://upload.wikimedia.org/wikipedia/commons/6/69/Flag_of_Sonora.svg"
# flag_tabasco = "https://upload.wikimedia.org/wikipedia/commons/b/b3/Flag_of_Tabasco.svg"
# flag_tamaulipas = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Tamaulipas.svg"
# flag_tlaxcala = "https://upload.wikimedia.org/wikipedia/commons/2/26/Flag_of_Tlaxcala.svg"
# flag_veracruz = "https://upload.wikimedia.org/wikipedia/commons/6/6a/Flag_of_Veracruz.svg"
# flag_yucatan = "https://upload.wikimedia.org/wikipedia/commons/9/9b/Flag_of_Yucatan.svg"
# flag_zacatecas = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Zacatecas.svg"
