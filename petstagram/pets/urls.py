from django.urls import path, include

from pets import views

urlpatterns = [
    path('add/', views.PetAddView.as_view(), name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.PetDetailsView.as_view(), name='pet-details'),
        path('edit/', views.pet_edit_view, name='edit-pet'),
        path('delete/', views.pet_delete_view, name='delete-pet'),
    ]))
]