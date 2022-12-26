
from django import forms
from section.models import Section
from extra_views import InlineFormSetFactory
from django.utils.translation import ugettext_lazy as _
from django.forms.models import BaseInlineFormSet


class SectionForm(forms.ModelForm):
    parent = forms.ModelChoiceField(label="parent", queryset=None, required=False)
    duration = forms.IntegerField(label="Duration in minutes", required=False,)
    error_messages = {
        "duplicate_section_name": _("A section with that name already exists."),
    }

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
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        queryset = Section.objects.filter(name=name)
        if self.instance.pk:
            if queryset.exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError(
                    self.error_messages["duplicate_section_name"], code="duplicate_section_name"
                )
        elif Section.objects.filter(name=name).exists():
            raise forms.ValidationError(self.error_messages["duplicate_section_name"], code="duplicate_section_name")
        return name

class ChildSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = (
            "name",
        )

class SectionInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super(SectionInlineFormSet, self).clean()
        if any(self.errors):
            return

        values = []
        deletes = []
        for form in self.forms:
            value = form.cleaned_data.get("name", None)
            delete = form.cleaned_data.get("DELETE", None)

            if value and value in values:
                raise forms.ValidationError("Duplicate Sub Section are not allowed")

            if delete is not None:
                deletes.append(delete)

            if value and not delete:
                values.append(value)

class SectionInline(InlineFormSetFactory):
    model = Section
    form_class = ChildSectionForm
    formset_class = SectionInlineFormSet
    factory_kwargs = {"extra": 0, "fk_name": "parent"}