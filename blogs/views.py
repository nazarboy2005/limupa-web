from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blogs.models import BlogModel, BlogTagModel, AuthorModel, BlogCategoryModel


class BlogsListView(ListView):
    template_name = 'blogs/blogs-list.html'
    model = BlogModel
    context_object_name = 'blogs'

    def get_queryset(self):
        blogs = BlogModel.objects.all().order_by('created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        if tag:
            blogs = blogs.filter(tags__in=tag)
        if cat:
            blogs = blogs.filter(categories__in=cat)

        return blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategoryModel.objects.all()
        context['tags'] = BlogTagModel.objects.all()
        blogs_data = self.get_queryset()
        context['recent_posts'] = blogs_data[:3]

        return context

