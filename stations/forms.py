from django import forms

from stations.models import Route
import re


class MixinFormControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'


class RouteForm(MixinFormControl, forms.ModelForm):
    class Meta:
        model = Route
        fields = ('start_point', 'end_point', 'name', 'height', 'weight', 'axel_load')

    def clean_start_point(self):
        start_point = self.cleaned_data.get('start_point', '')

        if not re.match(r'^\d+\.\d+\s\d+\.\d+$', start_point):
            raise forms.ValidationError('Неверный формат координат. Используйте формат "55.552137 49.487282".')

        return start_point

    def clean_end_point(self):
        end_point = self.cleaned_data.get('end_point', '')

        if not re.match(r'^\d+\.\d+\s\d+\.\d+$', end_point):
            raise forms.ValidationError('Неверный формат координат. Используйте формат "55.552137 49.487282".')

        return end_point
