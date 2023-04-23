from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

from rest_framework_simplejwt.authentication import JWTAuthentication

class MualliflarAPIView(generics.ListCreateAPIView): # get, post
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Muallif.objects.all()
    serializer_class = MuallifSerializer

    def get_queryset(self):
        soz = self.request.query_params.get('search')
        if soz: natija = Muallif.objects.filter(ism__contains=soz)
        else: natija = Muallif.objects.all()
        return natija

class MuallifDetailAPIView(generics.RetrieveUpdateDestroyAPIView): # get, put, del
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Muallif.objects.all()
    serializer_class = MuallifSerializer

class KitoblarAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer

    def get_queryset(self):
        soz = self.request.query_params.get('search')
        if soz: natija = Kitob.objects.filter(nom__contains=soz) | Kitob.objects.filter(muallif__ism__contains=soz)
        else: natija = Kitob.objects.all()
        return natija

class KitobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Kitob.objects.all()
    serializer_class = KitobSerializer

class TalabalarAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer

    def get_queryset(self):
        soz = self.request.query_params.get('search')
        if soz: natija = Talaba.objects.filter(ism__contains=soz)
        else: natija = Talaba.objects.all()
        return natija

class TalabaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer

class AdminlarAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def get_queryset(self):
        soz = self.request.query_params.get('search')
        if soz: natija = Admin.objects.filter(ism__contains=soz)
        else: natija = Admin.objects.all()
        return natija

class AdminDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class RecordlarAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get_queryset(self):
        soz = self.request.query_params.get('search')
        if soz: natija = (Record.objects.filter(talaba__ism__contains=soz) |
                          Record.objects.filter(kitob__nom__contains=soz) |
                          Record.objects.filter(olingan_sana__contains=soz))
        else: natija = Record.objects.all()
        return natija

class RecordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Record.objects.all()
    serializer_class = RecordSerializer