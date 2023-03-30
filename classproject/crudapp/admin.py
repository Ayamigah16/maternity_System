from django.contrib import admin

# Register your models here.
from crudapp.models import (Patient, Appointments, Meidical_Records,
                            Billings, Doctors, Obstetric_care, Neonatal_care)

admin.site.register(Patient)
admin.site.register(Appointments)
admin.site.register(Meidical_Records)
admin.site.register(Obstetric_care)
admin.site.register(Neonatal_care)
admin.site.register(Doctors)
admin.site.register(Billings)