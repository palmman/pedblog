from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post, Account

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'updated')
    prepopulated_fields = {'slug' :('title',)}

class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_login','date_joined', 'is_active')
    list_display_links = ('username', 'email')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Post, PostAdmin)
admin.site.register(Account, AccountAdmin)

