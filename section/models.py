from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(_("Section Name"), blank=True, max_length=255)
    duration = models.IntegerField(_("Duration"), blank=True, null=True)
    cut_off = models.PositiveSmallIntegerField(_("Cut Off"), default=0, blank=True)
    instructions = models.TextField(_("Instructions"), blank=True)
    max_num_of_questions_attemptable = models.PositiveSmallIntegerField(
        _("Maximum number of questions that can be attempted in the section"), blank=True, null=True
    )
    parent = models.ForeignKey("self", related_name="children", on_delete=models.CASCADE, null=True, blank=True)
    number_of_sections_to_attempt = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")

    def __str__(self):
        return self.name
