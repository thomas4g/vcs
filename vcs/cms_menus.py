from menus.base import NavigationNode, Menu
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class TestMenu(Menu):
    def get_nodes(self, request):
        return [NavigationNode(_('Portal'), '/portal/home', 1)]

menu_pool.register_menu(TestMenu)
