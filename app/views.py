import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from .models import Item

# Create your views here.
@api_view(['GET'])
def getData(request):
    item= Item.objects.all()
    serializer= ItemSerializer(item, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request): 
    serializer= ItemSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
    