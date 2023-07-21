import os
from typing import Any
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ElevatorManagementSystem.settings')
import django
django.setup()
from .models import Elevator,ElevatorSystem,ElevatorRequest
from myapp.api.serializers import ElevatorRequestSerializer
def select_elevator(current_floor,elevator_system):
    minimum_distance_from_current_floor = 99999999
    selected_elevator = None
    elevators = Elevator.objects.filter(elevator_system=elevator_system,is_working=True,is_available=True)
    for elevator in elevators:
        if abs(elevator.initial_floor-current_floor)<minimum_distance_from_current_floor:
            selected_elevator = elevator
            minimum_distance_from_current_floor=abs(elevator.initial_floor-current_floor)
    return selected_elevator


def arrange_requests(requested_floors,current_floor):
    requested_floors_sorted = sorted(requested_floors)
    upword_floors = []
    downword_floors = []
    arranged_floor_request = []
    for x in requested_floors_sorted:
        if x<current_floor:
            downword_floors.append(x)
        if x>current_floor:
            upword_floors.append(x)
    if current_floor in requested_floors:
        arranged_floor_request = [current_floor]
    if len(upword_floors)>len(downword_floors):
        arranged_floor_request.extend(upword_floors)
        arranged_floor_request.extend(downword_floors[::-1])
    else:
        arranged_floor_request.extend(downword_floors[::-1])
        arranged_floor_request.extend(upword_floors)
    return arranged_floor_request


def create_requests(selected_elevator,arranged_floor_requests):
    # try:
    request_list = []
    # for i in range(len(arranged_floor_requests)):
    #     if i==len(arranged_floor_requests)-1:
    #         request_list.append(ElevatorRequest(elevator=selected_elevator,current_floor=arranged_floor_requests[i],next_destination=arranged_floor_requests[i+1 if i<len(arranged_floor_requests) else None]))
    s=ElevatorRequest.objects.bulk_create(objs=[ElevatorRequest(elevator=selected_elevator,current_floor=arranged_floor_requests[i],next_destination=arranged_floor_requests[i+1] if i+1<len(arranged_floor_requests) else None) for i in range(len(arranged_floor_requests))])
    return ElevatorRequestSerializer(instance=s,many=True).data
    # except:
    #     return

def elevator_direction(elevator_instance):
    if elevator_instance.next_destination>elevator_instance.current_floor:
        return {"msg":"elevator in moving upwords","direction":1}
    else:
        return {"msg":"elevator in moving downwords","direction":-1}