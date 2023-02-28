#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Tuple

from book_manager.wildewidgets import BookTableWidget
from django.template.loader import render_to_string
from django.urls import reverse
from wildewidgets import (
    BreadcrumbBlock,
    CardWidget,
    Block,
    WidgetListLayoutHeader
)
from wildewidgets import __version__ as wildewidgets_version

from academy_theme import __version__ as theme_version
from academy_theme.wildewidgets import AcademyThemeMainMenu


#------------------------------------------------------
# Menus
#------------------------------------------------------

class MainMenu(AcademyThemeMainMenu):
    items: List[Tuple[str, str]] = [
        ('Home', 'core:home'),
        ('Wildewidgets Example', 'core:wildewidgets'),
    ]


class BaseBreadcrumbs(BreadcrumbBlock):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_breadcrumb('Home', reverse('core:home'))


#------------------------------------------------------
# Base Widgets
#------------------------------------------------------

class DatagridItem(Block):
    block: str = 'datagrid-item'
    title: str = None
    content: str = None

    def __init__(self, **kwargs):
        self.title = kwargs.pop('title', None)
        self.content = kwargs.pop('content', None)
        super().__init__(**kwargs)
        self.add_block(Block(self.title, name='datagrid-title'))
        self.add_block(Block(self.content, name='datagrid-content'))


class Datagrid(Block):
    block: str = 'datagrid'

    def add_item(self, title: str, content: str, **kwargs) -> None:
        """
        Add a :py:class:`DatagridItem` to contents.

        Args:
            title: the label for the item
            content: the content of the item
        """
        self.add_block(DatagridItem(title=title, content=content, **kwargs))


#------------------------------------------------------
# Widgets
#------------------------------------------------------

class ExampleTableWidget(BookTableWidget):
    title: str = 'dataTable Example'


#------------------------------------------------------
# Cards
#------------------------------------------------------

class AcademyInfoCardWidget(CardWidget):
    title: str = 'Academy Theme Info'
    icon: str = 'info-square'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        grid = Datagrid()
        grid.add_item('Theme Version', theme_version)
        grid.add_item('Wildewidgets Version', wildewidgets_version)
        grid.add_item('Tabler Version', '', css_id="tabler-version")
        grid.add_item('Bootstrap Icons Version', '', css_id="bootstrap-icons-version")
        grid.add_item('jQuery Version', '', css_id="jquery-version")
        grid.add_item('dataTables Version', '', css_id="datatables-version")
        self.widget = grid

    def get_content(self, **kwargs) -> str:
        """
        Append our Javasript to the end of our HTML.

        Returns:
            The content of our
        """
        content = super().get_content(**kwargs)
        content += render_to_string('core/version_js.html')
        return content
