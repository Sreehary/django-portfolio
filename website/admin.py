from django.contrib import admin

from .models import EducationInfo, ProfileInfo

admin.site.register(ProfileInfo)
admin.site.register(EducationInfo.Education)
