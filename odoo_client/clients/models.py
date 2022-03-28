from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    x_rc = models.CharField(null=True, blank=True, max_length=255)
    x_nif = models.CharField(null=True, blank=True, max_length=255)
    x_nis = models.CharField(null=True, blank=True, max_length=255)
    x_art = models.CharField(null=True, blank=True, max_length=255)
    is_person = models.BooleanField(default=False, null=True, blank=True)
    x_is_professional_non_commercial = models.BooleanField(
        default=False, null=True, blank=True
    )
    x_professional_identity_ref = models.CharField(
        null=True, blank=True, max_length=255
    )
    x_identity_ref_delevery_date = models.CharField(
        null=True, blank=True, max_length=255
    )
    x_identity_refissuing8quthority = models.CharField(
        null=True, blank=True, max_length=255
    )
