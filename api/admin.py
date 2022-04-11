from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import test, IndexPhotos, Publications, PublicationsMembers, PublicationsYears, IntroduceUs, AlumniMs, AlumniPhD, CustomUser, OurLabTopic
from .forms import CustomUserChangeForm, CustomUserCreationForm

admin.site.register(test)
admin.site.register(IndexPhotos)
admin.site.register(PublicationsYears)
admin.site.register(Publications)
admin.site.register(PublicationsMembers)
admin.site.register(IntroduceUs)
admin.site.register(AlumniMs)
admin.site.register(AlumniPhD)
admin.site.register(OurLabTopic)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email']


admin.site.register(CustomUser, CustomUserAdmin)
