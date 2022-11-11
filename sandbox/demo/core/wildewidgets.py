#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple

from academy_theme.wildewidgets import AcademyThemeMainMenu


#------------------------------------------------------
# Menus
#------------------------------------------------------

class MainMenu(AcademyThemeMainMenu):
    items: List[Tuple[str, str]] = [
        ('Home', 'core:home'),
    ]
