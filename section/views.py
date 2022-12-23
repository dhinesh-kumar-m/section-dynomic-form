# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.utils.translation import ugettext_lazy as _
from section.forms import ChildSectionForm, SectionForm
from extra_views import CreateWithInlinesView, NamedFormsetsMixin,InlineFormSetFactory

from section.models import Section
from django.urls import reverse_lazy

# Create your views here.

class SectionsListView(ListView):
    context_object_name = "sections"
    template_name = "sections/list.html"
    queryset = Section.objects.all()



class SectionInline(InlineFormSetFactory):
    model = Section
    form_class = ChildSectionForm
    factory_kwargs = {"extra": 4, "fk_name": "parent"}

class SectionsAddView(NamedFormsetsMixin, CreateWithInlinesView):
    model = Section
    form_class = SectionForm
    inlines = [SectionInline]
    inlines_names = ["child_sections"]
    template_name = "sections/form.html"
    success_message = _("Section added successfully.")
    success_url = reverse_lazy("sections:index")