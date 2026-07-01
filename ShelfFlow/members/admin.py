from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ["full_name", "member_code", "join_date"]
    fields = ["full_name", "phone_number"]
    readonly_fields = ['member_code', 'join_date']
    search_fields = ['full_name', 'member_code']

admin.site.register(Member, MemberAdmin)
