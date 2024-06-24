from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ProfileUpdateView, CompanyProfileUpdateView, EmergencyCollectionEditView, line_chart

urlpatterns = [
    path('', views.user_register, name='user_register'),
    path('company-register/', views.company_register, name='company_register'),
    path('login/', views.user_login, name='user_login'),
    path('company-login/', views.company_login, name='company_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('logouts/', views.company_logout, name='company_logout'),
    path('create-emergency/', views.create_emergency_collection, name='emergency'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('company-dashboard/', views.company_dashboard, name='company_dashboard'),  
    path('dd', views.home, name='home'), 
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('company-profile/', CompanyProfileUpdateView.as_view(), name='company_profile'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-emergency/<int:pk>/', EmergencyCollectionEditView.as_view(), name='edit_emergency'),
    # path('pie-chart/', pie_chart, name='pie_chart'),
    path('line-chart/', line_chart, name='line_chart'),
    path('create-illegal-deposit/', views.create_illegal_deposit, name='illegal-deposit'),
    path('pay-emergency/<int:collection_id>/', views.handle_payment, name='handle_payment'),
    path('submit-payment/', views.submit_payment, name='submit_payment'),
    path('find-paid-users/', views.find_paid_users, name='find_paid_users'),
]
