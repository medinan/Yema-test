from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class ScheduleDurationMINChoice:
    DURATION_15_MINUTES = 15
    DURATION_30_MINUTES = 30
    DURATION_45_MINUTES = 45
    DURATION_60_MINUTES = 60
    choices = (
        (DURATION_15_MINUTES, _("15 minutes")),
        (DURATION_30_MINUTES, _("30 minutes")),
        (DURATION_45_MINUTES, _("45 minutes")),
        (DURATION_60_MINUTES, _("60 minutes")),
    )


class ScheduleDaysChoice:
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    choices = (
        (MONDAY, _("monday")),
        (TUESDAY, _("tuesday")),
        (WEDNESDAY, _("wednesday")),
        (THURSDAY, _("thursday")),
        (FRIDAY, _("friday")),
        (SATURDAY, _("saturday")),
        (SUNDAY, _("sunday")),
    )


class ScheduleConfiguration(models.Model):
    doctor = models.ForeignKey("doctors.MedicalProfessional", on_delete=models.CASCADE, unique=True)
    schedule_duration = models.PositiveIntegerField(choices=ScheduleDurationMINChoice.choices)

    def __str__(self):
        return f"{self.doctor.name}-{self.schedule_duration}"


class ScheduleConfigurationDays(models.Model):
    schedule_configuration = models.ForeignKey(ScheduleConfiguration, on_delete=models.CASCADE)
    day = models.CharField(max_length=50, choices=ScheduleDaysChoice.choices)
    time_from = models.TimeField()
    time_to = models.TimeField()



