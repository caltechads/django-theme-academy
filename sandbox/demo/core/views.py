from typing import Any, Dict, Type

from django.views.generic import TemplateView
from wildewidgets import MenuMixin, BasicMenu
from wildewidgets import __version__ as wildewidgets_version

from academy_theme import __version__
from .wildewidgets import MainMenu


class HomeView(MenuMixin, TemplateView):
    """
    This view is here to test the non-wildewidgets base template.
    """
    template_name: str = "core/home.html"
    menu_class: Type[BasicMenu] = MainMenu
    menu_item: str = "Home"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        kwargs['version'] = __version__
        kwargs['wildewidgets_version'] = wildewidgets_version
        return super().get_context_data(**kwargs)
