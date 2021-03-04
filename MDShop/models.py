from django.db import models

from django.db import models 
from django.urls import reverse

from autoslug import AutoSlugField

from django.db.models.signals import pre_save
from django.db import models 

from datetime import date
from mptt.fields import  TreeForeignKey
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver



class Razdel(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)

    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Жанры"""
    name        = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url         = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
    def __str__(self):
        return "name: {}, id: {}".format(self.name, self.id)




class smartphone(models.Model):
    def __str__(self):
        return self.title

    img1     = models.ImageField(upload_to='photos',null=True, blank=True)
    img2     = models.ImageField(upload_to='photos',null=True, blank=True)
    img3     = models.ImageField(upload_to='photos',null=True, blank=True)
    img4     = models.ImageField(upload_to='photos',null=True, blank=True)
    img5     = models.ImageField(upload_to='photos',null=True, blank=True)
    img6     = models.ImageField(upload_to='photos',null=True, blank=True)
    title    = models.CharField(max_length=255)
    price    = models.PositiveSmallIntegerField("цена", default=2019)
    genres   = models.ManyToManyField(Genre, verbose_name="жанры")
    razdel   = models.ManyToManyField(Razdel, verbose_name="Категория")
    slug     = AutoSlugField(populate_from='title' )
    pred1=models.CharField(max_length=255,verbose_name='Диагональ дисплея, дюйм',blank=True)
    pred2=models.CharField(max_length=255,verbose_name='Разрешение дисплея',blank=True)
    pred3=models.CharField(max_length=255,verbose_name='Операционная система',blank=True)
    pred4=models.CharField(max_length=255,verbose_name='Объем оперативной памяти',blank=True)
    pred5=models.CharField(max_length=255,verbose_name='Объём встроенной памяти',blank=True)
    pred6=models.CharField(max_length=255,verbose_name='Количество SIM-карт',blank=True)
    pred7=models.CharField(max_length=255,verbose_name='Стандарт связи',blank=True)
    pred8=models.CharField(max_length=255,verbose_name='Стандарт защиты от пыли и влаги',blank=True)







    

    class Meta:
            ordering=['-id']
    def get_absolute_url(self):
            return reverse("blog:Post",args=[self.id,self.slug])



   

        
class Customer(models.Model):
    user       = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phone      = models.CharField(max_length=11,blank=True,null=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name  = models.CharField(max_length=30,null=True,blank=True)
    email      = models.EmailField(max_length=255,null=True,blank=True)
    
    class Meta:
            ordering=['-id']
    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)

    
    @receiver(post_save, sender=get_user_model())
    def create_likeCustomer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    
class CustomerLike(models.Model):
    
    likeNEW       =  models.ForeignKey(smartphone,  on_delete=models.CASCADE, null=True,blank=True)
    likeCustomer  =  models.ForeignKey(Customer,    on_delete=models.CASCADE, null=True           )
    created_at    =  models.DateTimeField(          auto_now_add=True,        null=True,blank=True)
    updated_at    =  models.DateTimeField(          auto_now=True,            null=True,blank=True)
    
    class Meta:
            ordering=['-id']
    @receiver(post_save, sender=Customer)
    def create_likeCustomer(sender, instance, created, **kwargs):
        if created:
            # if your user model has phone, if not remove phone.
            CustomerLike.objects.create(likeCustomer=instance)   



class CustomerAddress(models.Model):
    country          =      models.CharField(max_length=30,blank=True)
    town             =      models.CharField(max_length=30,blank=True)   
    address          =      models.CharField(max_length=30,blank=True)     
    house            =      models.CharField(max_length=30,blank=True)  
    apartment        =      models.CharField(max_length=30,blank=True)  
    index            =      models.CharField(max_length=30,blank=True)  
    addressCustomer  =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    class Meta:
            ordering =      ['-id']

class order(models.Model):
    orderCustomer    =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    smartphone       =      models.ManyToManyField(smartphone)
    orderAddress     =      models.ForeignKey(CustomerAddress, on_delete=models.CASCADE,null=True)
    price            =      models.PositiveSmallIntegerField("цена",blank=True,null=True)
    
    class Meta:
            ordering =      ['-id'] 


    
    
class PopularGoods(models.Model):
    top1=models.ManyToManyField(smartphone,blank=True,max_length=6)


class CustomerEnglish(models.Model):
    nameUser   = models.CharField(max_length=30,blank=True,null=True)
    phone      = models.CharField(max_length=11,blank=True,null=True)
    text       = models.CharField(max_length=233,null=True,blank=True)
    

class testModels(models.Model):
    USER             =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    text             =      models.CharField(max_length=330,blank=True)
    genres           =      models.ForeignKey(Genre, on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
            ordering =      ['-id'] 





class onHOLD(models.Model):
    USER             =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    text             =      models.CharField(max_length=330,blank=True)
    
    class Meta:
            ordering =      ['-id'] 

class inPROGRESS(models.Model):
    USER             =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    text             =      models.CharField(max_length=330,blank=True)
    
    class Meta:
            ordering =      ['-id'] 

class needsREVIEW(models.Model):
    USER             =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    text             =      models.CharField(max_length=330,blank=True)
    
    class Meta:
            ordering =      ['-id'] 

            

class APPROVED(models.Model):
    USER             =      models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    text             =      models.CharField(max_length=330,blank=True)
    
    class Meta:
            ordering =      ['-id'] 