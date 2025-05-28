from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render


def register(request: Request) -> HttpResponse:
    return render(request, 'accounts/register-page.html')


def login(request: Request) -> HttpResponse:
    return render(request, 'accounts/login-page.html')


def profile_details_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-details-page.html')


def edit_profile_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-delete-page.html')
