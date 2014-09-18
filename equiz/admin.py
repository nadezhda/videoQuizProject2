from django.contrib import admin
from equiz.models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner')


admin.site.register(Category)
admin.site.register(Section, PageAdmin)
admin.site.register(QuestionType)
admin.site.register(Question)
admin.site.register(Answer)


#admin.site.register(UserProfile)