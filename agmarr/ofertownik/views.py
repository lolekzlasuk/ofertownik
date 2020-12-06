
from django.shortcuts import render, get_object_or_404,redirect
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from .models import Offer,Product,ProductImage
from django.utils import timezone
from django.contrib import messages
from .forms import OfferForm
from . scraper import mainscrape
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
class IndexView(TemplateView):
    template_name = 'index.html'

class TemplateView(TemplateView):
        template_name = 'eng.html'
class OfferDetailView(DetailView):
    model = Offer


class OfferListView(LoginRequiredMixin,ListView):
    model = Offer
    def get_queryset(self):
        return Offer.objects.order_by('-date_created')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, 'Your password was updated successfully!')
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('account no active')
        else:
            print('failed login detected')
            print('username: {} and password {}'.format(username,password))
            return HttpResponse('invalid login details supplied')

    else:
        return render(request,'login.html',{})


@login_required
def create_offer(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)


        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('ofertownik:editoffer', slug = instance.slug)
    else:
        form = OfferForm()
    return render(request, 'ofertownik/offerform.html', {'form': form})

@login_required
def edit_offer(request,slug):
    context= {}
    offer = get_object_or_404(Offer,slug = slug)
    if request.method == 'POST' and request.is_ajax():
        pass
    else:
        offer = Offer.objects.get(slug = slug)
        context["offer"] = offer


        return render(request,'ofertownik/edit_offer.html',context)

@login_required
def addproduct(request):
    if request.method == 'POST' and request.is_ajax():
        pk = json.loads(request.body).get('pk')
        print(pk)
        offer = get_object_or_404(Offer,pk=pk)
        print(request.body)

        codelist = []
        codelist = json.loads(request.body).get('title').split(';')
        for e in codelist:
            prod = mainscrape(e)
            instance = Product.objects.create(
                offer = offer,
                name = prod['title'],
                price = prod['price'],
                description = prod['description'],
                material = prod['material'],
                size = prod['size'],
                link = prod['link']
                )
            print(prod['link'])
            for r in prod['photos']:
                imageinstance = ProductImage.objects.create(
                    product = instance,
                    adress = r
                )
        return HttpResponse("OK")

@login_required
def deleteproduct(request):
    if request.method == 'POST' and request.is_ajax():
        pk = json.loads(request.body).get('pk')
        product = get_object_or_404(Product,pk=pk)
        product.delete()
        return HttpResponse("OK")

@login_required
def editproduct(request):
    if request.method == 'POST' and request.is_ajax():
        pk = json.loads(request.body).get('pk')
        prod = json.loads(request.body)
        print(prod)
        product = get_object_or_404(Product,pk=pk)
        product.name = prod['title']
        product.price = prod['price']
        product.description = prod['description']
        product.material = prod['material']
        product.size = prod['size']
        product.save()
        return HttpResponse("OK")

@login_required
def deleteimage(request,pk):
    instance = get_object_or_404(ProductImage,pk=pk)
    offer = instance.product.offer
    slug = offer.slug
    instance.delete()
    return redirect('ofertownik:editoffer',slug = slug)

@login_required
def addimage(request,pk):
    if request.method == 'POST' and request.is_ajax():
        product = get_object_or_404(Product,pk=pk)
        instance = ProductImage.objects.create(
                product = product,
                adress = json.loads(request.body).get('adress')
        )
        return HttpResponse("OK")


def send_email(request):
    if request.method == 'POST' and request.is_ajax():
        mail = json.loads(request.body)
        print(mail)
        name = mail['name']
        surname = mail['surname']
        subject = mail['subject']
        message = mail['message']
        telephone = mail['telephone']
        mailfrom = mail['mailfrom']
        msg = EmailMessage(
            subject,
            "Wiadomość od: " + name +' '+ surname +"<br>" + "Email: " + mailfrom + "<br>" + "Numer telefonu: " + telephone + "<br>" + "Wiadomość: "+ "<br>" + message,
            mailfrom,
            ['biuro@pphagmar.pl'],

            )
        msg.content_subtype = "html"
        msg.send()
        return HttpResponse("OK")
