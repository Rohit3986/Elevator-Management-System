
from django.urls import path,include
from .views import *
urlpatterns = [
    path('elevator_system/create/',CreateElevatorSystem.as_view(),name="Create elevator system"),
    path('elevator/create',CreateElevator.as_view(),name='create elevator'),
    path('elevator/direction/<int:pk>',ElevatorDirection.as_view(),name='elevator direction'),
    path('elevator/floor_requests/<int:pk>',ElevatorFloorRequests.as_view(),name='floor requests'),
    path('elevator/door_open/<int:pk>',ElevatorDoorOpen.as_view(),name='door open'),
    path('elevator/door_close/<int:pk>',ElevatorDoorClose.as_view(),name='door close'),
    path('elevator_request/create',CreateElevatorRequests.as_view(),name='create elevator request'),
    path('elevator_request/process/<int:pk>',ProcessElevatorRequests.as_view(),name='process elevator request'),
]
