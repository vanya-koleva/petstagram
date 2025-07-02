from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

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


class PetEditView(UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self) -> str:
        return reverse(
            'pet-details',
            kwargs={
                'username': self.kwargs.get('username'),
                'pet_slug': self.kwargs.get('pet_slug'),
            }
        )


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
