from django.contrib import admin

from posts.models import Post, UserProfile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'user_posting', 'created_at')
	list_filter = ('user_posting', 'created_at')

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'fav_color', 'location', 'date_of_birth')
	
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
