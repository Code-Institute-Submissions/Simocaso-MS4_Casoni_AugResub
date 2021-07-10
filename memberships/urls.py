from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_memberships, name='memberships'),
    path('<membership_id>',views.memberships_detail,name='memberships_detail'),
]
