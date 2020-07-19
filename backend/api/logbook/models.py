# python imports
from string import ascii_uppercase

# django import
from django.db import models
from django.utils.translation import gettext_lazy as _


class LogBook(models.Model):
    CLASSES = [("nursery", _("Nursery")), ("lkg", _("LKG")), ("ukg", _("UKG"))] + [
        (str(i), _(str(i))) for i in range(1, 13)
    ]

    SECTIONS = [(a, a) for a in ascii_uppercase]

    teacher = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    subject = models.CharField(_("subject"), max_length=30)
    log_class = models.CharField(_("class"), choices=CLASSES, max_length=9)
    log_section = models.CharField(_("section"), choices=SECTIONS, max_length=3)
    time_start = models.TimeField(_("start time"))
    time_end = models.TimeField(_("end time"))
    date = models.DateField(_("date"))
    is_substitute = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("log book entry")
        verbose_name_plural = _("log book entries")

    def __str__(self):
        entry = (
            str(self.id)
            + "-"
            + self.teacher.get_full_name()
            + "-"
            + self.log_class
            + "-"
            + self.log_section
            + "-"
            + self.subject
        )
        return entry
