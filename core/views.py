from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import View, TemplateView


#def index(request):
#    return render(request, 'index.html')

class IndexView(TemplateView):
      template_name= 'index.html'

index = IndexView.as_view()




def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)


def product_list(request):
    return render(request, 'product_list.html')
