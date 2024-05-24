from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep
admin.site.unregister(Group)
# Register your models here.

#mix profile info into user info
class ProfileInLine(admin.StackedInline):
    model = Profile
#extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    #just display username fields on admin page
    fields = ["username"]
    inlines = [ProfileInLine]

#unredister intial user
admin.site.unregister(User)
#register the new user
admin.site.register(User, UserAdmin)

# admin.site.register(Profile)

# register meeps
admin.site.register(Meep)
