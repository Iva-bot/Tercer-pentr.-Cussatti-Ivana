from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Cliente, Producto, Envio, Proveedor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def inicio (request):
     return render(request, "AppSanta/index.html")

@login_required
def about(request):
     return render(request, "AppSanta/about.html")



class ClienteListView (LoginRequiredMixin, ListView):
     model = Cliente
     template_name ="/appsanta/Vista_Clases/cliente_list.html"

     def get(self,request,*args,**kwargs):
          return super().get(request,*args,**kwargs)

class ClienteDetalle (LoginRequiredMixin, DetailView):
     model= Cliente
     template_name="/appsanta/Vista_Clases/detalle.html"
    
class ClienteCreateViews (LoginRequiredMixin, CreateView):
     model = Cliente
     template_name = "/appsanta/Vista_Clases/cliente_form.html"
     success_url =reverse_lazy ("List")
     fields = ["nombre","cantidad"]

class ClienteUdateView (LoginRequiredMixin, UpdateView):
     model= Cliente
     template_name= "/appsanta/Vista_Clases/cliente_edit.html"
     #success_url =reverse_lazy ("List")
     success_url ="/AppSanta/clases/lista/"
     fields = ["nombre","cantidad"]

class ClienteDeleteView(LoginRequiredMixin, DeleteView):
     model = Cliente
     template_name = "/appsanta/Vista_Clases/cliente_confirm_delete.html"
     #success_url =reverse_lazy ("List")
     success_url ="/AppSanta/clases/lista/"
     fields = ["nombre","cantidad"]
