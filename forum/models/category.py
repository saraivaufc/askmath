from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

from ..utils.models import AutoSlugField

from .topic import Topic

class Category(models.Model):
	DRAFT = 'd'
	PUBLISHED = 'p'
	REMOVED = 'r'
	STATUS_CHOICES = (
		(DRAFT, _('Draft')),
		(PUBLISHED, _('Published')),
		(REMOVED, _('Removed')),
	)
	slug = AutoSlugField(populate_from="name", db_index=False, blank=True, unique=True)
	name = models.CharField(verbose_name=_("Name"), max_length=75)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES)
	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Created by"), related_name="category_created_by", blank=True)
	creation = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	def get_topics(self):
		return Topic.objects.filter(category=self, status='p')

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name', ]
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")