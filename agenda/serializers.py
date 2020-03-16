from rest_framework import serializers
from agenda.models import agendamentosModel

# Agenda Serializer
class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamentosModel
        fields = '__all__'