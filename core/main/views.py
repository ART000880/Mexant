from django.shortcuts import render
from django.views.generic import ListView
from .models import home,home1,hometest,service,service1,crypto,about,contact
# Create your views here.


class homeListView(ListView):
    template_name = 'index.html'

    def get(self,request):
        homes = home.objects.all()
        homes1 = home1.objects.all() 
        test = hometest.objects.all() 
        return render(request,self.template_name,{'homes':homes,'homes1':homes1,'test':test})


class serviceListView(ListView):
    template_name='our-services.html'

    def get(self,request):
        ser = service.objects.all()
        ser1 = service1.objects.all()
        crypt = crypto.objects.all()
        return render(request,self.template_name,{'ser':ser,'ser1':ser1,'crypt':crypt})


class aboutListView(ListView):
    template_name = 'about-us.html'

    def get(self,request):
        abt = about.objects.all()
        return render(request,self.template_name,{'abt':abt})    

class contactListView(ListView):
    template_name = 'contact-us.html'

    def get(self,request):
        cont = contact.objects.all()
        return render(request,self.template_name,{'cont':cont})             