from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details_view, name='profile-details'),
        path('edit/', views.edit_profile_view, name='edit-profile'),
        path('delete/', views.delete_profile_view, name='delete-profile')
    ]))
]