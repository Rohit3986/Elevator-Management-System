from myapp.models import *
from .serializers import *
from rest_framework import generics,status
from rest_framework.response import Response

from myapp import helper

class CreateElevatorSystem(generics.CreateAPIView):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer

class CreateElevator(generics.CreateAPIView):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer


class CreateElevatorRequests(generics.CreateAPIView):
    queryset = ElevatorRequest.objects.all()
    serializer_class = CreateElevatorRequestSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        current_floor,requested_floors,elevator_system = serializer.data['current_floor'],serializer.data['requested_floors'],ElevatorSystem.objects.first()
        selected_elevator = helper.select_elevator(current_floor,elevator_system)
        arranged_requests = helper.arrange_requests(requested_floors,current_floor)
        requests_created = helper.create_requests(selected_elevator,arranged_requests)
        if not requests_created:
            return Response({'msg':'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'msg':'floor requests submitted sucessfully','data':requests_created}, status=status.HTTP_201_CREATED)



class ProcessElevatorRequests(generics.RetrieveAPIView):
    serializer_class = CreateElevatorRequestSerializer
    queryset = ElevatorRequest.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            elevator_id = self.kwargs.get('pk')
            if elevator_id:
                instance = ElevatorRequest.objects.filter(elevator__id=elevator_id,is_visited=False).order_by('id').first()
                if not instance:
                    return Response({'msg':'no floor requets are available'})
            instance.is_visited = True
            instance.save()
            response = {"msg":"one floor request has been sucessfully processed for this elevator",
                        "visited_floor":instance.current_floor
                        }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'msg':'error occured','error':str(e)})
    

class ElevatorDirection(generics.RetrieveAPIView):
    serializer_class = CreateElevatorRequestSerializer
    queryset = ElevatorRequest.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            elevator_id = self.kwargs.get('pk')
            if elevator_id:
                instance = ElevatorRequest.objects.filter(elevator__id=elevator_id,is_visited=True).order_by('id').last()
                if not instance or not(instance.next_destination):
                    return Response({'msg':'elevator is not moving currently'})
            response = helper.elevator_direction(instance)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg':'error occured','error':str(e)})
    

class ElevatorFloorRequests(generics.RetrieveAPIView):
    serializer_class = CreateElevatorRequestSerializer
    queryset = ElevatorRequest.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            elevator_id = self.kwargs.get('pk')
            if elevator_id:
                instance = ElevatorRequest.objects.filter(elevator__id=elevator_id,is_visited=False).order_by('id')
                if not instance:
                    return Response({'msg':'no floor requets are available'})
            response = {"msg":"all pending floor requests are retrived for selected elevator","elevator_id":elevator_id,"floor_requests":ElevatorRequestSerializer(instance=instance,many=True).data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg':'error occured','error':str(e)})
        


class ElevatorDoorOpen(generics.RetrieveAPIView):
    serializer_class = ElevatorSerializer
    queryset = Elevator.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.is_door_open:
                response = {"msg":"door is already opened"}
            else:
                instance.is_door_open = True
                instance.save()
                response = {"msg":"door opened"}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg':'error occured','error':str(e)})
        
class ElevatorDoorClose(generics.RetrieveAPIView):
    serializer_class = ElevatorSerializer
    queryset = Elevator.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not(instance.is_door_open):
                response = {"msg":"door is already closed"}
            else:
                instance.is_door_open = False
                instance.save()
                response = {"msg":"door closed"}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg':'error occured','error':str(e)})