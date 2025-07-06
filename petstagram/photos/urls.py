from django.urls import path, include

from photos import views

urlpatterns = [
    path('add/', views.PhotoAddView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_view, name='photo-details'),
        path('edit/', views.photo_edit_view, name='edit-photo'),
        path('delete/', views.photo_delete_view, name='delete-photo'),
    ])),
]