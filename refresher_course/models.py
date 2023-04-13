from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model
from io import BytesIO
from django.core.files import File
import qrcode
from PIL import Image, ImageDraw

User = get_user_model()


class Course(models.Model):
    name = models.CharField(_("Kurs nomi"), max_length=255, null=True)
    language = models.CharField(_("Text"), max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False)
    hour_course = models.IntegerField(default=0)
    is_visible_hour = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Kurs')
        verbose_name_plural = _('Kurslar')


class Nation(models.Model):
    name = models.CharField(max_length=10)
    key = models.CharField(max_length=3, default='uz')
    status = models.BooleanField(_("Status"), default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Millat')
        verbose_name_plural = _('Millatlar')


def user_directory_path(instance, filename):
    return 'files/{0}/{1}-{2}/{3}'.format(str(instance.course.id), str(instance.start_date), instance.month, filename)


class CourseComplete(models.Model):
    Months = (
        ('yanvar', _('Yanvar')),
        ('fevral', _('Fevral')),
        ('mart', _('Mart')),
        ('aprel', _('Aprel')),
        ('may', _('May')),
        ('iyun', _('Iyun')),
        ('iyul', _('Iyul')),
        ('avgust', _('Avgust')),
        ('sentabr', _('Sentabr')),
        ('oktabr', _('Oktabr')),
        ('noyabr', _('Noyabr')),
        ('dekabr', _('Dekabr')),
    )
    Years = (
        ('2021', _('2021')),
        ('2022', _('2022')),
        ('2023', _('2023')),
        ('2024', _('2024')),
        ('2025', _('2025')),
        ('2026', _('2026')),
        ('2027', _('2027')),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.CharField(_("Kurs boshlangan kun"), max_length=3, null=True, blank=True)
    end_date = models.CharField(_("Kurs tugagan kun"), max_length=3, null=True, blank=True)
    month = models.CharField(_("Oy"), max_length=50, default="yanvar", choices=Months)
    begin_cer_nomer = models.BigIntegerField(_("Boshlang'ich raqam"), default=0, null=True)
    nationality = models.ForeignKey(Nation, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(_("Fayl"), upload_to=user_directory_path)
    year = models.CharField(_("Yil"), max_length=4, default="2023", choices=Years)
    CERTIFICATE_CHOICES = (
        ("1", "Ilmiy o'quv markazi"),
        ("2", "Guruh nazoratchilari"),
    )
    certificate_turi = models.CharField(_("Certificate turi"), max_length=1, default=1, choices=CERTIFICATE_CHOICES)

    def save(self, *args, **kwargs):
        if not self.nationality:
            self.nationality = Nation.objects.get(id=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.course.name

    class Meta:
        ordering = ['-id']


class Certificate(models.Model):
    Months = (
        ('yanvar', _('Yanvar')),
        ('fevral', _('Fevral')),
        ('mart', _('Mart')),
        ('aprel', _('Aprel')),
        ('may', _('May')),
        ('iyun', _('Iyun')),
        ('iyul', _('Iyul')),
        ('avgust', _('Avgust')),
        ('sentabr', _('Sentabr')),
        ('oktabr', _('Oktabr')),
        ('noyabr', _('Noyabr')),
        ('dekabr', _('Dekabr')),
    )
    Years = (
        ('2021', _('2021')),
        ('2022', _('2022')),
        ('2023', _('2023')),
        ('2024', _('2024')),
        ('2025', _('2025')),
        ('2026', _('2026')),
        ('2027', _('2027')),
    )
    first_name = models.CharField(_('Familiya'), max_length=100, blank=True, null=True)
    last_name = models.CharField(_('Ism'), max_length=100, blank=True, null=True)
    middle_name = models.CharField(_('Otasini ismi'), max_length=30, null=True, blank=True, default=" ")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.CharField(_("Kurs boshlangan kun"), max_length=3, null=True, blank=True)
    end_date = models.CharField(_("Kurs tugagan kun"), max_length=3, null=True, blank=True)
    month = models.CharField(_("Oy"), max_length=50, default="yanvar", choices=Months)
    year = models.CharField(_("Yil"), max_length=4, default="2023", choices=Years)
    cer_nomer = models.BigIntegerField(_("Sertifikat raqami"), default=0, null=True)
    qr_code = models.ImageField(_("QR Code"), upload_to='qr_codes/', blank=True, null=True)
    status = models.BooleanField(_("Status"), default=True)
    nationality = models.ForeignKey(Nation, on_delete=models.CASCADE, null=True, blank=True)
    passport = models.CharField(_('Pasport'), max_length=15, blank=True, null=True)
    jshshr = models.BigIntegerField(_('Jshshr'), blank=True, null=True)
    invoice = models.BigIntegerField(_('Invoice'), blank=True, null=True)
    registered_number = models.BigIntegerField(_("Registratsiya nomeri"), default=0, null=True)
    registered_day = models.CharField(_('Registeratsiya sanasi'), max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    pdf_certificate = models.FileField(upload_to="pdfs")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"

    class Meta:
        verbose_name = _('Sertifikat')
        verbose_name_plural = _('Sertifikatlar')


class Page(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    value = models.PositiveBigIntegerField(default=5, unique=True)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
