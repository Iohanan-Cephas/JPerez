from django.db import models

class Redirect(models.Model):
    slug = models.CharField(max_length=20, unique=True)
    target_url = models.URLField()
    total_accesses = models.PositiveIntegerField(default=0)
    last_access = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.slug} -> {self.target_url}"
