from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from django.conf import settings

from base.utils.models import AutoSlugField

from .topic import Topic

STATUS_CHOICES = (
	('d', _('Draft')),
	('p', _('Published')),
	('r', _('Removed')),
)

class Category(models.Model):
	name = models.CharField(verbose_name=_("Name"), max_length=75)
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"User"), blank=True)


	def __unicode__(self):
		return self.name

	def get_topics(self):
		return Topic.objects.filter(category=self, status='p')

	class Meta:
		ordering = ['name', ]
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")