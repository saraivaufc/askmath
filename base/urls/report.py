from django.conf.urls import include, url
from django.contrib.auth.decorators import permission_required
from django.utils.translation import ugettext_lazy as _

from ..views import ReportCreateView

urlpatterns = [
	url(_(r'^add$'), ReportCreateView.as_view(), name="report_create"),
]