from django.urls import path
from blogs.views import BlogsListView, BlogDetailsView

app_name = 'blogs'


urlpatterns = [
    path('', BlogsListView.as_view(), name='list'),
    path('details/<int:pk>/', BlogDetailsView.as_view(), name='details')
]