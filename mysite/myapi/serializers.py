from rest_framework import serializers
from .models import Author

class AuthorSerializers(serializers.Serializer):
    # class Meta:
    #     model = Author
    #     fields = "__all__"
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    age = serializers.IntegerField(allow_blank=True)

    def create(self, validated_data):
        return Author.create.objects(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        return instance