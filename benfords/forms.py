from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, ButtonHolder, Submit

from benfords.models import DataSet


class DataSetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.use_custom_control = False
        self.helper.layout = self.form_layout()

    def form_layout(self):
        return Layout(
            Row(
                Field('input_file'),
            ),
            Row(
                ButtonHolder(
                    Submit('submit', 'Send', css_class='btn btn-primary btn-sm'),
                ),
                css_class='mt-4'
            )

        )

    class Meta:
        model = DataSet
        fields = ('input_file', )
