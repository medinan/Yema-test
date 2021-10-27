from django.contrib import admin

from apps.schedule.models import ScheduleConfiguration, ScheduleConfigurationDays


class ScheduleConfigurationAdmin(admin.ModelAdmin):
    pass


class ScheduleConfigurationDaysAdmin(admin.ModelAdmin):
    pass


admin.site.register(ScheduleConfiguration, ScheduleConfigurationAdmin)
admin.site.register(ScheduleConfigurationDays, ScheduleConfigurationDaysAdmin)
