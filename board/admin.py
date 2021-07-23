from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Post, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['subject','content']
    list_display = ['id','subject','short_content','author','create_date']
    list_display_links = ['id', 'subject']
    list_filter = ['author',]

    def short_content(self, post):
        return post.content[:30]

class CategoryAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
        'title',
        
    )
    # prepopulated_fields = {'slug': ('title',)}
    mptt_level_indent = 20


admin.site.register(Category, CategoryAdmin)


admin.site.register(Post, PostAdmin)
