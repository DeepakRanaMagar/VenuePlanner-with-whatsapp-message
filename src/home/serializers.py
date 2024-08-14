from rest_framework import serializers

from accounts.models import Media, Venue


class VenueSerializer(serializers.ModelSerializer):
    '''
        Handles serialization for the Venue Model Data for browse by property and price also the search fields
    '''
    class Meta:
        model = Venue
        fields = ['id','organization_name','logo', 'property_type', 'rating',
                  'seat_capacity']
        

class MediaSerializer(serializers.ModelSerializer):
    '''
        Handles serializer for the Media files
    '''

    class Meta:
        model = Media
        fields = '__all__'