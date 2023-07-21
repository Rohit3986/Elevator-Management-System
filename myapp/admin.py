from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ElevatorSystem)
class ElevatorSystemAdmin(admin.ModelAdmin):
    list_display = ["id","total_elevators","total_floors","created_at","modified_at"]

@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ["id","is_working","elevator_system","initial_floor","created_at","modified_at"]

@admin.register(ElevatorRequest)
class ElevatorRequestAdmin(admin.ModelAdmin):
    list_display = ["id","elevator","current_floor","next_destination","is_visited","created_at","modified_at"]