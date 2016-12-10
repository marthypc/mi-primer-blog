#Todas las líneas que comienzan con from o import son líneas para agregar algo de otros archivos

from django.db import models
from django.utils import timezone


class Post(models.Model):						#esto define el modelo; es un objeto
												#class define q estamos haciendo un modelo
												#Post es el nombre de nuestor modelo
												#models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
   #aquí se definen los propiedades
   # le decimos que tipo es cada variable
    author = models.ForeignKey('auth.User')		#vinculo con otro modelo
    title = models.CharField(max_length=200)	#de tipo caracter - 200 de largo
    text = models.TextField()					##tipo texto - largo sin limite
    created_date = models.DateTimeField(		##DE TIPO FECHA Y HR
            default=timezone.now)
    published_date = models.DateTimeField(		#tipo fecha y hr
            blank=True, null=True)

    def publish(self):							#publish es el nombre del método
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title