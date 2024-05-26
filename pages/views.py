from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        form.save()

        return render(self.request, 'error-success-messages/contact-success.html')

    def form_invalid(self, form):
        print(form.errors)
        print(form.cleaned_data['name'])

        return render(self.request, 'error-success-messages/contact-error.html')


class AboutView(TemplateView):
    template_name = 'about-us.html'

