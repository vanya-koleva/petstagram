from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from common.forms import CommentForm
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


class PetAddView(CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs) -> dict:
        kwargs.update({
            'comment_form': CommentForm(),
            'all_photos': self.object.photo_set.prefetch_related('tagged_pets', 'like_set').all(),
        })
        return super().get_context_data(**kwargs)


def pet_edit_view(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('pet-details', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-edit-page.html', context)


def pet_delete_view(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    form = PetDeleteForm(instance=pet)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    context = {
        'form': form,
        'pet': pet,
    }

    return render(request, 'pets/pet-delete-page.html', context)
