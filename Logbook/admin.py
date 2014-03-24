from django.contrib import admin
from Logbook.models import Visit, Diagnosis, Procedure

def index(self, *args, **kwargs):
     return admin.site.__class__.index(self, extra_context={'title':'TEST Practice'}, *args, **kwargs)
admin.site.index = index.__get__(admin.site, admin.site.__class__)


class VisitAdmin(admin.ModelAdmin):
    list_display = ["patient", "datetime", "status", "clinic", "provider"]
    fieldsets = [
        (None, {'fields': ['patient', 'clinic', 'provider']}),
    ]
    list_filter = ["clinic", "status", "provider", "datetime"]
    raw_id_fields = ('patient',)
    autocomplete_lookup_fields = {
        'fk': ['patient'],
    }


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ["code", "sh_desc"]
    search_fields = ["sh_desc", "desc"]

class ProcedureAdmin(admin.ModelAdmin):
    list_display = ["code", "sh_desc"]
    search_fields = ["sh_desc", "desc"]

admin.site.register(Visit, VisitAdmin)
#admin.site.register(Diagnosis, DiagnosisAdmin)
#admin.site.register(Procedure, ProcedureAdmin)
