#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Tuple

from django.templatetags.static import static

from wildewidgets import (
    CardWidget,
    Datagrid,
    VerticalDarkMenu,
)
from wildewidgets import __version__ as wildewidgets_version

from academy_theme import __version__ as theme_version


#------------------------------------------------------
# Menus
#------------------------------------------------------

class AcademyThemeMainMenu(VerticalDarkMenu):
    brand_image: str = static("academy_theme/images/logo.png")
    brand_image_width: str = "100%"
    brand_text: str = "Academy Theme"
    items: List[Tuple[str, str]] = [
        ('Home', 'core:home'),
        ('Wildewidgets', 'core:wildewidgets')
    ]


#------------------------------------------------------
# Cards
#------------------------------------------------------

class AcademyInfoCardWidget(CardWidget):
    card_title: str = f'Version {theme_version}'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        grid = Datagrid()
        grid.add_item('Wildewidgets Version', wildewidgets_version)
        grid.add_item('Tabler Version', '', css_id="tabler-version")
        grid.add_item('Bootstrap Icons Version', '', css_id="bootstrap-icons-version")
        grid.add_item('jQuery Version', '', css_id="jquery-version")
        self.set_widget(grid)
