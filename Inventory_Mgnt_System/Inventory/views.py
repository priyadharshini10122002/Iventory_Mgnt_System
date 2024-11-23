from .models import Items
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ItemsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ItemsAPI(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    
    def get(self,request,id=None):
        if id:
            try:
               obj=Items.objects.get(item_id=id)
               serializer=ItemsSerializer(obj)
               return Response(serializer.data)
            except Items.DoesNotExist:
                return Response({'Message : Item Not Exist !'},status=status.HTTP_404_NOT_FOUND)
        
        else:
            ob=Items.objects.all()
            serializer=ItemsSerializer(ob,many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        
    def post(self,request):
        data = request.data
        serializer=ItemsSerializer(data=data)
        id=data['item_id']
        if Items.objects.filter(item_id=id).exists():
            return Response({'Message : Item Already Exist !'},status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
    
    def put(self,request,id):
          try:
              obj=Items.objects.get(item_id=id)
          except Items.DoesNotExist:
            return Response({'Message : Item Not Exist !'},status=status.HTTP_404_NOT_FOUND)
          serializer=ItemsSerializer(obj,data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
          return Response(data=serializer.errors,status=status.HTTP_200_OK)              

    def delete(self,request,id):
        try:
            obj=Items.objects.get(item_id=id)
        except Items.DoesNotExist:
            return Response({'Message : Item Not Exist !'},status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response ({'The Item Deleted Successfully !'},status=status.HTTP_200_OK)


        # item=Items.objects.get(Item_id=id).DoesNotExist()
        # if item:
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors) 
            
        # else:
        #     return Response({'Message : Item Already Exist !'})

    # def patch(self,request,id):
    #       try:
    #         obj=Items.objects.get(item_id=id)

    #         serializer=ItemsSerializer(obj,data=request.data,partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({serializer.data},status=status.HTTP_200_OK)
    #         return Response(serializer.errors)     
    #       except Items.DoesNotExist:
    #         return Response({'Message : Item Not Exist !'},status=status.HTTP_400_BAD_REQUEST)


