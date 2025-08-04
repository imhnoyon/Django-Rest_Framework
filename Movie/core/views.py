from django.shortcuts import render
import django_filters
from .serializers import MovieSerializers,ReviewSerializers
from .models import Movielist,Reviews

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsreviewerorReadonly

from .pagination import MoviePageNumberPagination,MovieLimitOffsetPagination,MovieCursorPagination
# @api_view(['GET', 'POST'])
# # post mane data create kora
# def Movielists(request):
#     if request.method =='GET':
#         movies=Movielist.objects.all()
#         serialisers=MovieSerializers(movies,many=True)
#         return Response(data=serialisers.data)

#     elif request.method =='POST':
#         serialisers =MovieSerializers(data=request.data)
#         if serialisers.is_valid():
#             serialisers.save()
#             return Response(serialisers.data,status=status.HTTP_201_CREATED)
        
#         return Response(serialisers.errors,status=status.HTTP_404_NOT_FOUND)
    

# @api_view(['GET','PUT','PATCH','DELETE'])
# get mane all data dekha
# put mane update kora
# patch mane specific kono data update kora
# delete mane data delete kora
# def MovieUpdate(request,pk):
#     movies=get_object_or_404(Movielist,pk=pk)
#     if request.method =='GET':
#         serialisers=MovieSerializers(movies)
#         return Response(data=serialisers.data)

#     elif request.method =='PUT':
#         serialisers =MovieSerializers(movies,data=request.data)
#         if serialisers.is_valid():
#             serialisers.save()
#             return Response(serialisers.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serialisers.errors,status=status.HTTP_404_NOT_FOUND)        
        
#     elif request.method == 'PATCH':
#         serialisers =MovieSerializers(movies,data=request.data, partial=True)
#         if serialisers.is_valid():
#             serialisers.save()
#             return Response(serialisers.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serialisers.errors,status=status.HTTP_404_NOT_FOUND)
        
#     elif request.method =='DELETE':
#         movies.delete()
#         return Response({'status':'Movie delte successfully !!'})




# List of all movies, create a new movies
# class MoiveListCreateView(generics.ListCreateAPIView):
#     queryset =Movielist.objects.all()
#     serializer_class=MovieSerializers


# single movie retrive kora update kora delete kora
# class MovieDetailsview(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Movielist.objects.all()
#     serializer_class =MovieSerializers



# list of all review , new create review
# class ReviewListCreateView(generics.ListCreateAPIView):
#     queryset =Reviews.objects.all()
#     serializer_class=ReviewSerializers

# single reviews,update,delete

# class ReviewsDetailsview(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Reviews.objects.all()
#     serializer_class =ReviewSerializers



class MoiveListCreateView(viewsets.ModelViewSet):
    queryset=Movielist.objects.prefetch_related('reviews') #m2m  , foreign key related kaj kore 
    serializer_class=MovieSerializers
    pagination_class=MovieCursorPagination



class ReviewListCreateView(viewsets.ModelViewSet):
    queryset=Reviews.objects.select_related('movie')
    serializer_class=ReviewSerializers
    # permission_classes = [IsreviewerorReadonly,IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['reviewer__username', 'rating']
    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)