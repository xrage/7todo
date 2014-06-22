'''
 :author: "Dharmendra Verma"
 :copyright: "Copyright 2013, Shopsense.Co" 
 :created: 22/06/14
 :email: "dharmendraverma@shopsense.co"   
 :github: @xrage 

'''

from django.contrib import admin
from app.models import Todo, Company, CompanyUser


class ToDoAdmin(admin.ModelAdmin):
    list_filter = ("todo", "created_by", "created_on", "modified_on")
    search_fields = ("created_by",)

class CompanyAdmin(admin.ModelAdmin):
    list_filter = ("company", "website", "created_by", "registered_on")
    search_fields = ("created_by",)

class CompanyUserAdmin(admin.ModelAdmin):
    list_filter = ("company", "user", "token", "state")
    search_fields = ("state", "company",)

# class UserProfileAdmin(admin.ModelAdmin):
#     list_filter = ("user",)
#     filter_horizontal = ("company",)


admin.site.register(Todo, ToDoAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyUser, CompanyUserAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)

