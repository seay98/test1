from .models import Client, Poster
from rest_framework import routers, serializers, viewsets
import json

# Serializers define the API representation.
class ClientSerializer(serializers.ModelSerializer):

    default_error_messages = {'error': 'Data validation failed.'}

    class Meta:
        model = Client
        fields = ['curl', 'passwd', 'ipaddr', 'port']
   
    # def validate(self, attrs):
    #     uname = attrs.get('uname')
    #     if uname == '1':
    #         raise serializers.ValidationError(
    #             self.default_error_messages)
    #     return attrs

class PosterSerializer(serializers.HyperlinkedModelSerializer):

    default_error_messages = {'error': 'Data validation failed.'}

    class Meta:
        model = Poster
        fields = ['content', 'reporter']

    def validate(self, attrs):
        content = attrs.get('content')
        try:
            content = json.loads(content)
        except ValueError:
            raise serializers.ValidationError(self.default_error_messages)
        return attrs