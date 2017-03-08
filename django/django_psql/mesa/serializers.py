from rest_framework import serializers
from .models import Mesa

class MesaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Mesa
		fields = ('nombre', 'tipoPedido','valor')
		#fields = '__all__'