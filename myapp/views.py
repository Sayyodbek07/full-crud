from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class PersonCrud(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonCreate(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(f"Ma'lumotlaringiz yaraldi {serializer.data}", status=status.HTTP_200_OK)

class PersonUpdate(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer