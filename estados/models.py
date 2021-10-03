from django.db import models

# left = value, right = description

category_list = ( 
    ("Tour en pie", "Tour en pie"), 
    ("Tour en carro", "Tour en carro"), 
    ("Tour en aire", "Tour en aire"), 
    ("Eventos", "Eventos"),
    ("Retro", "Retro"),
) 

# States
class Aguascalientes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

class BajaCalifornia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title


class BajaCaliforniaSur(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title


class Campeche(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title
    

class Chiapas(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title


class Chihuahua(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title
    

class Coahuila(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title


class Colima(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class CiudadDeMexico(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Durango(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Guanajuato(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Guerrero(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Hidalgo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Jalisco(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class EstadoDeMexico(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Michoacan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Morelos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Nayarit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class NuevoLeon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Oaxaca(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Puebla(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Queretaro(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class QuintanaRoo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class SanLuisPotosi(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Sinaloa(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Sonora(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Tabasco(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Tamaulipas(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Tlaxcala(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Veracruz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Yucatán(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title

        
class Zacatecas(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city_tag = models.CharField(max_length=100)
    tag1 = models.CharField(max_length=20)
    tag2 = models.CharField(max_length=20)
    tag3 = models.CharField(max_length=20, blank=True)
    tag4 = models.CharField(max_length=20, blank=True)
    url = models.URLField(null=True)
    image_url = models.URLField(blank=True)
    
    category_tag = models.CharField( 
        max_length = 20, 
        choices = category_list, 
        default = 'walking'
        )
    
    def __str__(self):
        return self.title