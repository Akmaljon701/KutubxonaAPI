from rest_framework.serializers import ModelSerializer
from .models import *

class MuallifSerializer(ModelSerializer):
    class Meta:
        model = Muallif
        fields = '__all__'

    def to_representation(self, instance):
        muallif = super().to_representation(instance)
        muallif['kitoblari'] = KitobSerializer(Kitob.objects.filter(muallif=instance), many=True).data

        return muallif

class KitobSerializer(ModelSerializer):
    class Meta:
        model = Kitob
        fields = '__all__'

class TalabaSerializer(ModelSerializer):
    class Meta:
        model = Talaba
        fields = '__all__'

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'