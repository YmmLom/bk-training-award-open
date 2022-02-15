from awards_apply.models import AwardApplicationRecord
from rest_framework import serializers


class ApplicationSerializer(serializers.ModelSerializer):
    application_users = serializers.JSONField()

    class Meta:
        model = AwardApplicationRecord
        field = "__all__"
