from django.contrib import admin

from scard.models import Club, Course, Scorecard


class CourseInline(admin.StackedInline):
    model = Course
    extra = 1


class ClubAdmin(admin.ModelAdmin):
    inlines = (CourseInline,)
    list_display = ('id', 'name', 'location')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'club', 'name')


class ScorecardAdmin(admin.ModelAdmin):
   
    list_display = ('id','club', 'course', 'owner', 'create_dt')


admin.site.register(Club, ClubAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Scorecard, ScorecardAdmin)
