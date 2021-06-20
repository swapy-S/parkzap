from rest_framework import serializers
from .models import Details

class formSerializer(serializers.ModelSerializer):
	class Meta:
		model = Details
		fields = ['name','dob','email','number']