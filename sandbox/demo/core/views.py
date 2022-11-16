from typing import Any, Dict, Type

from django.views.generic import TemplateView
from wildewidgets import (
    BasicMenu,
    MenuMixin,
    StandardWidgetMixin,
    WidgetListLayout
)
from wildewidgets import __version__ as wildewidgets_version

from academy_theme import __version__
from .wildewidgets import (
    AcademyInfoCardWidget,
    BaseBreadcrumbs,
    MainMenu,
    ExampleTableWidget
)


class HomeView(TemplateView):
    """
    This view is here to test the non-wildewidgets base template.
    """
    template_name: str = "core/home.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        kwargs['version'] = __version__
        kwargs['wildewidgets_version'] = wildewidgets_version
        kwargs['menu'] = str(MainMenu('Home'))
        return super().get_context_data(**kwargs)


class WildewidgetsView(
    MenuMixin,
    StandardWidgetMixin,
    TemplateView
):
    """
    This view is here to test the non-wildewidgets base template.
    """
    template_name: str = "academy_theme/base--wildewidgets.html"
    menu_class: Type[BasicMenu] = MainMenu
    menu_item: str = "Wildewidgets Example"

    def get_content(self):
        layout = WidgetListLayout("Wildewidgets Example")
        layout.add_widget(AcademyInfoCardWidget())
        layout.add_widget(ExampleTableWidget())
        return layout

    def get_breadcrumbs(self):
        breadcrumbs = BaseBreadcrumbs()
        breadcrumbs.add_breadcrumb('Wildewidgets')
        return breadcrumbs
