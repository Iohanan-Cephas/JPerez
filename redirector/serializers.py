from .models import Redirect
from rest_framework import serializers

class RedirectSerializer(serializers.ModelSerializer):
    clicks = serializers.IntegerField(read_only=True)
    last_access = serializers.DateTimeField(read_only=True)
    qr_code_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Redirect
        fields = ['slug', 'target_url', 'last_access', 'qr_code_url', 'clicks']

    def get_qr_code_url(self, obj):
        if obj.qr_code:
            return obj.qr_code.url
        return None

    def validate_slug(self, value):
        if self.instance is None and Redirect.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Esse slug já existe. Escolha outro.")
        if self.instance and self.instance.slug != value:
            if Redirect.objects.filter(slug=value).exists():
                raise serializers.ValidationError("Esse slug já existe. Escolha outro.")
        return value