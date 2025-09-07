from django.contrib import admin
from website.models import Contact,Newsletter
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','subject','email','created_date','update_date')
    list_filter = ('subject',)
    ordering = ('created_date',)
    search_fields = ('title','content')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)


# Register your models here.
