from django.db import models

# Create your models here.


class home(models.Model):
    name = models.CharField('home name',max_length = 200)
    about = models.TextField('home about')
    image = models.ImageField('home img',upload_to = 'media')

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'home'
        verbose_name_plural = 'homes' 

class home1(models.Model):
    name = models.CharField('home name',max_length = 200)
    about = models.TextField('home about')
    name1 = models.CharField('home name1',max_length = 200)
    about1 = models.TextField('home about1')
    name2 = models.CharField('home name2',max_length = 200)
    about2 = models.TextField('home about2')
    name3 = models.CharField('home name3',max_length = 200)
    about3 = models.TextField('home about3')
    name4 = models.CharField('home name4',max_length = 200)
    about4 = models.TextField('home about4')
    name5 = models.CharField('home name5',max_length = 200)
    about5 = models.TextField('home about5')

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'home1'
        verbose_name_plural = 'homes1' 


class hometest(models.Model):
    name = models.CharField('hometest name',max_length = 200)
    about = models.TextField('hometest about')
    image = models.ImageField('hometest img',upload_to = 'media')

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'hometest'
        verbose_name_plural = 'hometests' 



class service(models.Model):
    name = models.CharField('service name',max_length = 200)
    image = models.ImageField('service img',upload_to = 'media')

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'service'
        verbose_name_plural = 'services' 

class service1(models.Model):
    name = models.CharField('service1 name',max_length = 200)
    about = models.TextField('service1 about')
    image = models.ImageField('service1 img',upload_to = 'media')

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'service1'
        verbose_name_plural = 'services1' 

class crypto(models.Model):
    name = models.CharField('crypto name',max_length = 200)
    name1 = models.CharField('crypto name1',max_length = 200)
    name2 = models.CharField('crypto name2',max_length = 200)
    about = models.TextField('crypto about')
    about1 = models.TextField('crypto about1')
    about2 = models.TextField('crypto about2')
    text = models.TextField('crypto text')
    text1 = models.TextField('crypto text1')
    text2 = models.TextField('crypto text2')
    char = models.TextField('crypto char')
    char1 = models.TextField('crypto char1')
    char2 = models.TextField('crypto char2')
    image = models.ImageField('crypto img',upload_to = 'media')
    image1 = models.ImageField('crypto img1',upload_to = 'media')
    image2 = models.ImageField('crypto img2',upload_to = 'media')

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'crypto'
        verbose_name_plural = 'cryptos'         


class about(models.Model):
    name = models.CharField('about name',max_length = 200)
    about = models.TextField('about')
    name1 = models.CharField('about name1',max_length = 200)
    about1 = models.TextField('about1')
    name2 = models.CharField('about name2',max_length = 200)
    about2 = models.TextField('about2')
    image = models.ImageField('about img',upload_to = 'media')
    
    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'   


class contact(models.Model):
    name = models.CharField('service1 name',max_length = 200)
    about = models.TextField('service1 about')
    image = models.ImageField('service1 img',upload_to = 'media')

    def __str__(self):
        return self.name

    class meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts' 