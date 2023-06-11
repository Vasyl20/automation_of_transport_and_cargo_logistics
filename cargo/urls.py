from django.urls import path
from . import views
from .views import CarListView, CarCreateView, FuelListView, FuelCreateView

app_name = 'cargo'


urlpatterns = [
    path('cargo-list/', CargoListView.as_view(), name='cargo-list'),
    path('create/', views.CargoCreateView.as_view(), name='cargo-create'),
    # path('cargo/<int:pk>/', views.CargoDetailView.as_view(), name='cargo-detail'),
    # path('cargo/<int:pk>/update/', views.CargoUpdateView.as_view(), name='cargo-update'),
    # path('cargo/<int:pk>/delete/', views.CargoDeleteView.as_view(), name='cargo-delete'),

    # path('company/', CompanyListView.as_view(), name='company-list'),
    # path('company/create/', CompanyCreateView.as_view(), name='company-create'),
    # path('company/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    # path('company/<int:pk>/update/', CompanyUpdateView.as_view(), name='company-update'),
    # path('company/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
    #
    # # Driver URLs
    # path('driver/', DriverListView.as_view(), name='driver-list'),
    # path('driver/create/', DriverCreateView.as_view(), name='driver-create'),
    # path('driver/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
    # path('driver/<int:pk>/update/', DriverUpdateView.as_view(), name='driver-update'),
    # path('driver/<int:pk>/delete/', DriverDeleteView.as_view(), name='driver-delete'),
    #
    # # Car URLs
    path('car-list/', views.CarListView.as_view(), name='car-list'),
    path('car/create/', views.CarCreateView.as_view(), name='car-create'),
    # path('car/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    # path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    # path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    #
    # # Fuel URLs
    path('fuel/list/', views.FuelListView.as_view(), name='fuel-list'),
    path('fuel/create/', views.FuelCreateView.as_view(), name='fuel-create'),
    # path('fuel/<int:pk>/', FuelDetailView.as_view(), name='fuel-detail'),
    # path('fuel/<int:pk>/update/', FuelUpdateView.as_view(), name='fuel-update'),
    # path('fuel/<int:pk>/delete/', FuelDeleteView.as_view(), name='fuel-delete'),
    #
    # # Logistician URLs
    # path('logistician/', LogisticianListView.as_view(), name='logistician-list'),
    # path('logistician/create/', LogisticianCreateView.as_view(), name='logistician-create'),

]