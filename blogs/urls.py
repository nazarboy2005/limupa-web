from django.urls import path
from blogs.views import BlogsListView

app_name = 'blogs'


urlpatterns = [
    path('', BlogsListView.as_view(), name='list')
]