from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mesa
from .serializers import MesaSerializer

#lista de todas las mesas o para crear una nueva :)
class MesaList(APIView):

	def get(self, request):
		mesas = Mesa.objects.all()
		serializer = MesaSerializer(mesas, many=True)
		return Response(serializer.data)

	def post(self):
		pass