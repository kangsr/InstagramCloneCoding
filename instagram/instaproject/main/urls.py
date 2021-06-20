from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('accounts/', include('account.urls')),
    path('feed/<int:id>', views.detail, name='detail'),
    path('feed/new/', views.new, name='new'),
    path('feed/create', views.create, name='create'),
    path('feed/delete/<int:id>', views.delete, name='delete'),
    path('feed/edit/<int:id>', views.edit, name='edit'),
    path('feed/update/<int:id>' , views.update, name='update'),
    path('profile/<int:author_id>', views.profile, name='profile'),
]