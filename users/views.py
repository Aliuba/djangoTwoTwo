from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# class UserView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('hello from get')
#
#     def put(self, *args, **kwargs):
#         return Response('hello from put')
#
#     def post(self, *args, **kwargs):
#         return Response('hello from post')
#
#     def patch(self, *args, **kwargs):
#         return Response('hello from patch')
#
#     def delete(self, *args, **kwargs):
#         return Response('hello from delete')
from users.models import UserModel

from .serialized import UserSerializer


class ListCreateView(APIView):

    def get(self, *args, **kwargs):
        # db_users = UserModel.objects.all()
        # users = UserSerializer(db_users, many=True).data
        # print(users)
        # return Response(users, status.HTTP_200_OK)
        qs = UserModel.objects.all()
        # qs = qs.filter(age__gt=15)
        # print(qs)
        # get = UserModel.objects.get(name='max')
        # get = UserModel.objects.all()[2:4]
        # user = UserSerializer(get, many=True).data
        name = self.request.query_params.get('name')
        if name:
            qs=qs.filter(name__iexact=name)
        user = UserSerializer(qs, many=True).data
        return Response(user)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDeleteView(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        print(pk)
        user = get_object_or_404(UserModel.objects.all(), pk=pk)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(instance, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENTз)
