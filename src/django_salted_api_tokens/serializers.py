from rest_framework import serializers

from django_salted_api_tokens.settings import (DEFAULT_TOKEN_ID_LENGTH,
                                               DEFAULT_TOKEN_LENGTH)


class TokenResponseSerializer(serializers.Serializer):
    token_id = serializers.CharField(max_length=DEFAULT_TOKEN_ID_LENGTH)
    token = serializers.CharField(max_length=DEFAULT_TOKEN_LENGTH)
    message = serializers.CharField(
        default='These credentials will be lost forever if not stored now'
    )
