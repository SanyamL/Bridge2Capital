from rest_framework import serializers
from english.models import ContactUsContactForm

class ContactFormFilled(serializers.ModelSerializer):
    class Meta:
        model = ContactUsContactForm
        fields = '__all__'