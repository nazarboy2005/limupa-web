from django.views.generic import TemplateView, ListView
from django.views.generic import TemplateView, ListView

from blogs.models import BlogModel, BlogTagModel, BlogCategoryModel


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


class BlogDetailsView(TemplateView):
    template_name = 'blogs/blog-details.html'
    model = BlogModel

    def get_context_data(self, **kwargs):
        context = dict()
        context['categories'] = BlogCategoryModel.objects.all()
        context['tags'] = BlogTagModel.objects.all()
        context['recent_posts'] = BlogModel.objects.all().order_by('created_at')[:3]
        context['blog'] = BlogModel.objects.get(id=self.kwargs["pk"])

        return context
