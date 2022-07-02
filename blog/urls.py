from django.urls import path
from .views import blogListView, blogDetailView, blogCreateView, blogUpdateView

urlpatterns=[
    path('post/<int:pk>/edit/', blogUpdateView.as_view(), name='post_edit'),
    path('post/new', blogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', blogDetailView.as_view(), name='post_detail'),
    path('', blogListView.as_view(), name='home'),
]