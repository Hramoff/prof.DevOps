from django import forms


class Registration(forms.Form):
    login = forms.CharField(
        min_length=2,
        max_length=60,
        widget=forms.TextInput(
           attrs={
               'placeholder': 'Логин'
           }
        )
    )
    email = forms.EmailField(
        min_length=1,
        max_length=60,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Электронная почта'
            }
        )
    )
    password = forms.CharField(
        min_length=1,
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Пароль'
            }
        )
    )


class auth(forms.Form):
    log_auth = forms.CharField(
        min_length=2,
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ваш Логин'
            }
        )
    )
    pass_auth = forms.CharField(
        min_length=2,
        max_length=60,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ваш Пароль'
            }
        )
    )