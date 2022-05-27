from django.forms import ModelForm

from personages.models import Personage


class PersonageCreateForm(ModelForm):
    class Meta:
        model = Personage
        fields = '__all__'
        exclude = ('id', 'user_id')

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name)
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        self.instance.user_id = self._user
        return super().save(commit)