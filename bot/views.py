from rest_framework import generics

from bot.models import ObjectPart, Block
from bot.serializers import ObjectPartSerializer, BotSerializer


class BlockList(generics.ListCreateAPIView):
    queryset = Block.objects.all()
    serializer_class = BotSerializer


class ObjectPartList(generics.ListCreateAPIView):
    queryset = ObjectPart.objects.all()
    serializer_class = ObjectPartSerializer


class ObjectPartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObjectPart.objects.all()
    serializer_class = ObjectPartSerializer

    def put(self, request, *args, **kwargs):
        number_now = ObjectPart.objects.filter(id=self.kwargs['pk']).values_list()[0][5]
        ObjectPart.objects.filter(order_number=request.data['order_number']).update(order_number=number_now)
        return self.update(request, *args, **kwargs)
