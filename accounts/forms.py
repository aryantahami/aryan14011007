from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:  # برای اینکه اطلاعات اضافه به فرممون بدیم از متا استفاده میکنیم
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):  # 127-6
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
