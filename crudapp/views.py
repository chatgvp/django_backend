# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['POST'])
def create_value(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data, "message": "Hello world"}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def display_values(request):
    values = MyModel.objects.all()
    serializer = MyModelSerializer(values, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def display_value(request, pk):
    try:
        value = MyModel.objects.get(pk=pk)
        serializer = MyModelSerializer(value)  # Remove many=True
        return Response(serializer.data)
    except MyModel.DoesNotExist:
        return Response({'error': 'Value not found.'}, status=404)

@api_view(['PUT'])
def update_value(request, pk):
    try:
        value = MyModel.objects.get(pk=pk)
        serializer = MyModelSerializer(value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except MyModel.DoesNotExist:
        return Response({'error': 'Value not Found'}, status=404)
    
@api_view(['GET'])
def delete_value(request, pk):

    try:
        value = MyModel.objects.get(pk=pk)
        value.delete()
        return Response({"message":"Deleted Successfully"})
    except MyModel.DoesNotExist:
        return Response({'error': 'Value not found'})