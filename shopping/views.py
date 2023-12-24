from rest_framework.views import APIView
from .serializers import ShoppingListSerializer, ShoppingListItemSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from shopping.models import ShoppingList, ShoppingListItem

class ShoppingList(APIView):

    def post(self, request: Request):
        serializer = ShoppingListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        shopping_lists = ShoppingList.objects.all()
        
        serializer = ShoppingListSerializer(shopping_lists, many=True)
        return Response(serializer.data)

    def delete(self, request: Request):
        pass

class ShoppingListItem(APIView):
    
    def post(self, request: Request):
        pass

    def get(self, request: Request):
        pass

    def delete(self, request: Request):
        pass
