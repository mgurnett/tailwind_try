from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import *
from .serializers import *

@api_view(['GET'])
def getData (request):
    items = Reading.objects.all()
    serializer = ReadingSerializer(items, many=True)
    return Response(serializer.data)   

@api_view(['POST'])
def addReading(request):
    print(request.data)
    for reading in request.data:
        sensor_w1_id = reading["sensor"]
        try:
            sensor = Sensor.objects.get(wire1_id=sensor_w1_id)
        except Sensor.DoesNotExist:
            return Response({"error": "Sensor not found"}, status=404)

        reading["sensor"] = sensor.id  # Use sensor.id instead of sensor

    serializer = ReadingSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

'''
curl -X POST -H 'Content-Type: application/json' -d '{"recorded": "2024-12-18T16:17:15.341648Z", "value": 15.0, "sensor": 1}' http://127.0.0.1:8000/api/add/
curl -X POST -H 'Content-Type: application/json' -d '{"recorded": "2024-12-18T21:21:41.799476Z", "value": 9.5, "sensor": 61}' http://127.0.0.1:8000/api/add/
'''


@api_view(['POST'])
def addStatus(request):
    print(request.data)
    chain_post = request.data["chain"]
    try:
        chain_object = Chain.objects.get(ip=chain_post)
    except Chain.DoesNotExist:
        return Response({"error": "Chain not found"}, status=404)

    request.data["chain"] = chain_object.id

    serializer = StatusSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
'''
curl -X POST -H 'Content-Type: application/json' -d '{"recorded": "2025-01-18T16:17:15", "battery": 3.7, "chain": "10.70.70.139"}' http://127.0.0.1:8000/api/status/
'''