from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    name = models.CharField(
        max_length=30
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")
            super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
