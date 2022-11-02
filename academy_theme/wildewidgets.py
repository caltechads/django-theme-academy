#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.templatetags.static import static

from wildewidgets import VerticalDarkMenu


#------------------------------------------------------
# Menus
#------------------------------------------------------

class AcademyThemeMainMenu(VerticalDarkMenu):
    brand_image: str = static("academy_theme/images/logo.png")
    brand_image_width: str = "100%"
    brand_text: str = "Academy Theme"
