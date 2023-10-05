from . import serializers


class RestrictInactiveUsersMixins:
    def get_serializer_class(self):
        if not self.request.user.is_active:
            return serializers.UserUpdateModelSerializer 
        else:
            return serializers.UserUpdateModelSerializer           