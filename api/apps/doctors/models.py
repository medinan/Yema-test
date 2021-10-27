from django.db import models


class MedicalSpeciality(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MedicalProfessional(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.ForeignKey(MedicalSpeciality, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}({self.speciality.name})"



