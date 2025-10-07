from django.db import models

class Redirect(models.Model):
    slug = models.SlugField(max_length=20, unique=True)
    target_url = models.URLField()
    last_access = models.DateTimeField(blank=True, null=True)
    qr_code = models.ImageField(upload_to="qrcodes/", blank=True, null=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.slug} -> {self.target_url}"
