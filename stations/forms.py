from django import forms

from stations.models import Route


class MixinFormControl:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'


class RouteForm(MixinFormControl, forms.ModelForm):
    class Meta:
        model = Route
        fields = ('start_point', 'end_point', 'height', 'weight', 'axel_load')
