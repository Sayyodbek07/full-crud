
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductsList
from .serialzeries import ProductsSerializers

class ProductsListCreateApiView(APIView):
    def get(self, request):
        persons = ProductsList.objects.all()
        serializer = ProductsSerializers(persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductsUpdateDestroyApiView(APIView):
    def get_object(self, pk):
        try:
            return ProductsList.objects.get(pk=pk)
        except ProductsList.DoesNotExist:
            return None

    def put(self, request, pk):
        your_object = self.get_object(pk)
        if not your_object:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductsSerializers(your_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        your_object = self.get_object(pk)
        if not your_object:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductsSerializers(your_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        your_object = self.get_object(pk)
        if not your_object:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        your_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
