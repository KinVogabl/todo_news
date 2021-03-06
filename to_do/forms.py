from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = 'Пароль должен содержать минимум 8 цифр и 2 буквы'
        self.fields['password2'].help_text = ''
