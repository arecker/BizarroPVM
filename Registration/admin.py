from django.contrib import admin
from django.contrib.admin.models import LogEntry
from Registration.models import Patient, Clinic, Physician, Employer

# Customizes home page header
def index(self, *args, **kwargs):
     return admin.site.__class__.index(self, extra_context={'title':'TEST Practice'}, *args, **kwargs)
admin.site.index = index.__get__(admin.site, admin.site.__class__)

class PatientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'birthday', 'street', 'city', 'state', 'zip', 'employer', 'physician']
    fieldsets = [
        ('General Information', {'fields': ['social_security', 'last_name', 'first_name', 'middle_name', 'sex', 'birthday', 'employer', 'physician']}),
        ('Contact Information', {'fields': ['street', 'street_second', 'city', 'state', 'zip', 'phone']}),
        ('Notes', {'fields': ['notes']}),
    ]
    ordering = ['last_name', 'first_name']
    list_filter = ['physician', 'employer', ]
    search_fields = ["last_name", "first_name", "street", "city"]


class ClinicAdmin(admin.ModelAdmin):
    list_display = ['short', 'description', 'contact', 'street', 'city', 'state', 'zip']
    fieldsets = [
        ('General Information', {'fields': ['short', 'description', 'contact', 'street', 'street_second', 'city', 'state', 'zip', 'phone']}),
        ('Billing Information', {'fields': ['attn', 'bill_street', 'bill_unit', 'bill_city', 'bill_state', 'bill_zip']})
    ]
    ordering = ['short']
    search_fields = ["short", "description", "contact"]

class PhysicianAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'active']
    fieldsets = [
        ('General information', {'fields': ['account', 'last_name', 'first_name', 'middle_name']}),
        ('None', {'fields': ['active', 'member', 'ref_physician', 'uses_sched']}),
        ('Billing Information', {'fields': ['UPIN', 'NPI', 'fed_tax_id', 'taxonomy_code']}),
    ]
    ordering = ["last_name", "first_name"]
    list_filter = ["active", "member", "ref_physician", "uses_sched"]
    search_fields = ["last_name", "first_name"]



class EmployerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'street', 'city', 'state', 'zip', 'phone', 'verified', 'status']
    fieldsets = [
        ('Contact Information', {'fields': ['name', 'contact', 'street', 'street_second', 'city', 'state', 'zip', 'phone']}),
        ('Billing Information', {'fields': ['verified', 'status', 'statement_type', 'print_statement', 'print_ssn', 'payment_term']}),
    ]
    ordering = ["name"]
    list_filter = ["verified", "status", "statement_type"]
    search_fields = ["name", "contact", "street"]

class LogEntryAdmin(admin.ModelAdmin):
    list_display = [LogEntry.__str__, 'user', 'action_time']
    list_filter = ['user']

# Register Models
admin.site.register(Patient, PatientAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Physician, PhysicianAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(LogEntry, LogEntryAdmin)