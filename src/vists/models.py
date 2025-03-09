from django.db import models
class PageVists(models.Model):
    page = models.TextField(blank=True, null=True)
    timestamps =   models.DateTimeField(auto_now_add=True)


