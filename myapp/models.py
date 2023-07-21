from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class ElevatorSystem(models.Model):
    total_elevators = models.PositiveIntegerField()
    total_floors = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Elevator System : {self.id}'

class Elevator(models.Model):
    is_working = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)
    elevator_system = models.ForeignKey(to=ElevatorSystem,related_name="elevators",on_delete=models.PROTECT)
    initial_floor = models.PositiveIntegerField()
    is_door_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Elevator : {self.id}'
    

class ElevatorRequest(models.Model):
    elevator = models.ForeignKey(to=Elevator,related_name="elevator_logs",on_delete=models.PROTECT)
    current_floor = models.PositiveIntegerField()
    next_destination = models.PositiveIntegerField(default=None,null=True,blank=True)
    is_visited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)