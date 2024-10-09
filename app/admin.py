from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'view_content', )
    search_fields = ('title', 'short_description')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('-created_at',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'created_at', 'updated_at', )
    search_fields = ('first_name', 'last_name', 'position', )
    list_filter = ('position', 'created_at', )
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    ordering = ('-created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'view_count', 'created_at', 'updated_at',)
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'team_member', 'slug', 'created_at', 'updated_at',)
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_active', 'created_at', 'updated_at',)
    search_fields = ('content',)
    ordering = ('-created_at',)