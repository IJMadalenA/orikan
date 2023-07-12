from rest_framework.serializers import (
    ModelSerializer,
    DateTimeField,
)


class BaseBinanceSerializerInput(ModelSerializer):
    created_at = DateTimeField(
        help_text="Created at.",
        required=False,
        allow_null=True,
    )
    updated_at = DateTimeField(
        help_text="Updated at.",
        required=False,
        allow_null=True,
    )

    class Meta:
        abstract = True
        fields = [
            'created_at',
            'updated_at',
        ]
