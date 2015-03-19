from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PortalApphook(CMSApp):
    name = _("Portal")
    urls = ["portal.urls"]

apphook_pool.register(PortalApphook)
