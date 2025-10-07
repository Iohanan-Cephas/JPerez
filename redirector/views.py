from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.files.base import ContentFile
from django.utils import timezone
from django.contrib import messages
from django.db import IntegrityError
from django.views import View

from .models import Redirect

from io import BytesIO
import qrcode

# Create your views here.
# You can add view functions here to handle requests and render templates.
# For example:
# def home(request):
#     return render(request, 'home.html')

class HomeView(View):
    def get(self, request):
        redirects = Redirect.objects.all()
        return render(request, 'redirector/home.html', {'redirects': redirects})

    def post(self, request):
        slug = request.POST.get('slug')
        if Redirect.objects.filter(slug=slug).exists():
            messages.error(request, f'O slug "{slug}" já existe!')
            return redirect('home')
        target_url = request.POST.get('target_url')

        redirect_obj = Redirect(slug=slug, target_url=target_url)

        public_url = request.build_absolute_uri(f'/r/{slug}/')
        qr_img = qrcode.make(public_url)
        buffer = BytesIO()
        qr_img.save(buffer, format="PNG")
        redirect_obj.qr_code.save(f'{slug}_qrcode.png', ContentFile(buffer.getvalue()), save=False)

        redirect_obj.save()
        return redirect('home')

class RedirectSlugView(View):
    def redirect_slug(self, request, slug):
        redirect_obj = get_object_or_404(Redirect, slug=slug)
        redirect_obj.clicks += 1
        redirect_obj.last_access = timezone.now()
        redirect_obj.save()
        return HttpResponseRedirect(redirect_obj.target_url)

class EditRedirectView(View):
    def get(self, request, id):
        redirect_obj = get_object_or_404(Redirect, id=id)
        return render(request, 'redirector/edit_redirect.html', {'redirect': redirect_obj})

    def post(self, request, id):
        redirect_obj = get_object_or_404(Redirect, id=id)
        redirect_obj.target_url = request.POST.get('target_url')
        redirect_obj.save()
        return redirect('home')

class DeleteRedirectView(View):
    def post(self, request, id):
        redirect_obj = get_object_or_404(Redirect, id=id)
        redirect_obj.delete()
        return redirect('home')