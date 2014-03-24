from django.db import models
from Registration.models import Patient, Clinic, Physician

class Visit(models.Model):
    status_choices = [
        (1, "Logged"),
        (2, "Charting"),
        (3, "Charged"),
        (4, "Billed"),
    ]
    clinic = models.ForeignKey(Clinic, verbose_name="Clinic")
    status = models.IntegerField(choices=status_choices, default=1)
    patient = models.ForeignKey(Patient, verbose_name="Patient")
    provider = models.ForeignKey(Physician, verbose_name="Provider")
    datetime = models.DateTimeField(auto_now_add=True, blank=True)


class Diagnosis(models.Model):
    code = models.CharField(max_length=5, verbose_name="Code")
    sh_desc = models.CharField(max_length=20, verbose_name="Short Description")
    desc = models.TextField(max_length=200, verbose_name="Long Description")
    visit = models.ForeignKey(Visit, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Diagnoses"

class Procedure(models.Model):
    code = models.CharField(max_length=5, verbose_name="Code")
    sh_desc = models.CharField(max_length=20, verbose_name="Short Description")
    desc = models.TextField(max_length=200, verbose_name="Long Descripton")
    visit = models.ForeignKey(Visit, null=True, blank=True)