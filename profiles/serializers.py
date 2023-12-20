from rest_framework import serializers

from profiles.models import Profiles


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'
        # fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'country', 'image', 'user')



