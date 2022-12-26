# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.utils.translation import ugettext_lazy as _
from extra_views import CreateWithInlinesView, NamedFormsetsMixin,UpdateWithInlinesView

from section.forms import SectionForm,SectionInline
from section.models import Section
from django.urls import reverse_lazy

# Create your views here.

class SectionsListView(ListView):
    context_object_name = "sections"
    template_name = "sections/list.html"
    queryset = Section.objects.filter(parent__isnull=True)


class SectionsAddView(NamedFormsetsMixin, CreateWithInlinesView):
    model = Section
    form_class = SectionForm
    inlines = [SectionInline]
    inlines_names = ["child_sections"]
    template_name = "sections/form.html"
    success_message = _("Section added successfully.")
    success_url = reverse_lazy("sections:index")

class SectionUpdateView(NamedFormsetsMixin, UpdateWithInlinesView):
    model = Section
    form_class = SectionForm
    inlines = [SectionInline]
    inlines_names = ["child_sections"]
    template_name = "sections/form.html"
    success_message = _("Section Updated successfully.")
    success_url = reverse_lazy("sections:index")