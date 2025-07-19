from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        data.update({
            "username": user.username,
            "email": user.email,
            "designation": user.designation if hasattr(user, "designation") else "",
            "is_admin": user.is_superuser,
        })

        return data
