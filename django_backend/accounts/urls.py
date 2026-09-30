from django.urls import path
from .views import RegisterView, ProfileView, LogoutView, AddCardView, CardListView, DeleteCardView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cards/', AddCardView.as_view(), name='add-card'),
    path('cards/list/', CardListView.as_view(), name='card-list'),
    path('cards/<int:pk>/', DeleteCardView.as_view(), name='delete-card'),
]