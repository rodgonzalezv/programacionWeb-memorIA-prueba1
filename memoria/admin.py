from django.contrib import admin
from .models import Familiar, Plan, PlanCliente

# Register your models here.
admin.site.register(Familiar)
admin.site.register(Plan)
admin.site.register(PlanCliente)