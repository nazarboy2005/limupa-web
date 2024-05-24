from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def form_valid(self, form):
        form.save()

        return render(self.request, 'error-success-messages/contact-success.html')

    def form_invalid(self, form):
        return render(self.request, 'error-success-messages/contact-error.html', context={'errors': form.errors})
