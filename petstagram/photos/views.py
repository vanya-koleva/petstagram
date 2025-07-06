from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.forms import CommentForm
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')


def photo_details_view(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def photo_edit_view(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')
