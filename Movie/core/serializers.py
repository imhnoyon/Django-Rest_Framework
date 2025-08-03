from rest_framework import serializers
from .models import Movielist,Reviews


class ReviewSerializers(serializers.ModelSerializer):
    reviewer=serializers.StringRelatedField()
    
    class Meta:
        model = Reviews
        fields = '__all__' 

class MovieSerializers(serializers.ModelSerializer):
    # nested serializer and must name related name hbe eikhane from model
    reviews=ReviewSerializers(many=True,read_only=True)
    # reviews=serializers.StringRelatedField(many=True,read_only=True) #string related ralation
    # reviews=serializers.PrimaryKeyRelatedField(many=True,read_only=True) #primary key related ralation
    # reviews = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie_details')
    class Meta:
        model = Movielist
        fields = '__all__' 