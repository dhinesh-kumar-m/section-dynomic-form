
from django import forms
from django.forms.models import inlineformset_factory
from section.models import Section


class SectionForm(forms.ModelForm):
    parent = forms.ModelChoiceField(label="parent", queryset=None, required=False)
    duration = forms.IntegerField(label="Duration in minutes", required=False,)

    class Meta:
        model = Section
        fields = (
            "name",
            "duration",
            "cut_off",
            "instructions",
            "parent",
            "number_of_sections_to_attempt",
        )

class ChildSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = (
            "name",
        )
