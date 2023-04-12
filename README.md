# django-theme-academy

`django-theme-academy` provides the Academy theme for Django websites and applications.  Academy provides the following features:

* Built with Tabler, and Bootstrap 5
* A fixed left sidebar with configurable logo
* Breadcrumbs
* A footer with contact information for your organiization
* Includes [django-wildewidgets](https://github.com/caltechads/django-wildewidgets) support

## Installation

`django-theme-academy` supports Python 3.7+, and Django 3+.

To install from PyPI:

```bash
pip install django-theme-academy
```

### Update settings.py

Register the module in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'academy_theme',
    ...
]
```

Add the custom template context processor:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            ...
            'context_processors': [
                ...
                'academy_theme.context_processors.theme',
                ...
            ],
        },
    },
]
```

Optionally configure the theme specific settings.  You don't need to define all of these, but instead
only the ones you wish to override:

```python
ACADEMY_THEME_SETTINGS = {
    # Header
    'APPLE_TOUCH_ICON': 'myapp/images/apple-touch-icon.png',
    'FAVICON_32': 'myapp/images/favicon-32x32.png',
    'FAVICON_16': 'myapp/images/favicon-16x16.png',
    'FAVICON': 'myapp/images/favicon.ico',
    'SITE_WEBMANIFEST': 'myapp/images/site.webmanifest',

    # Footer
    'ORGANIZATION_LINK': 'https://myorg.com',
    'ORGANIZATION_NAME': 'Organization Name',
    'ORGANIZATION_ADDRESS': 'Organization Address',
    'COPYRIGHT_ORGANIZATION': 'Copyright Organization'
    'FOOTER_LINKS': []
}
```

### Choose a base.hml

`django-theme-academy` ships with two different base templates:

* `academy_theme/base.html`, for regular Django template development
* `academy_theme/base--wildewidgets.html`, for [django-wildewidgets](https://github.com/caltechads/django-wildewidgets) based Django development

#### base.html

To use `academy_theme/base.html`, create your own `base.html` that extends it
and overrides its blocks as needed.  Example:

```html
{% extends 'academy_theme/base.html' %}
{% load static academy_theme i18n %}

{% block title %}{% trans 'My App Title' %}{% endblock %}

{% block extra_css %}
  <link rel="stylesheet" href="{% static 'myapp/css/styles.css' %}">
{% endblock %}

{% block extra_header_js %}
  <script src="{% static 'myapp/js/app.js %}" ></script>
{% endblock %}

{% block menu %}
<nav class="navbar navbar-vertical navbar-expand-lg navbar-dark">
 <div class="container-lg ms-0">
    <a class="navbar-brand" href="#">
        <img src="{% static 'myapp/images/logo.png' %} alt="My App" width="100%">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContentV_9628" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-1">
       <li class="nav-item">
          <a class="nav-link" href="/">Home</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
{% endblock %}

{% block breadcrumbs %}
  <ol class="breadcrumb">
    {% block breadcrumb-items %}
        {% breadcrumb 'Home' 'myapp:home' %}
    {% endblock %}
  </ol>
{% endblock %}
```

#### base-wildewidgets.html

If you don't need to add any Javascript or CSS, this can be used directly in
your ``django-wildewidgets`` based views, like so:

```python
from typing import List, Tuple, Type

from academy_theme.wildewidgets import AcademyThemeMainMenu
from django.templatetags.static import static
from wildewidgets import (
    BasicMenu,
    BreadcrumbBlock
    CardWidget,
    MenuMixin,
    StandardWidgetMixin,
    WidgetListLayout
)

class MainMenu(AcademyThemeMainMenu):
    brand_image: str = static("myapp/images/logo.png")
    brand_text: str = "My App"
    items: List[Tuple[str, str]] = [
        ('Home', 'myapp:home'),
    ]


class BaseBreadcrumbs(BreadcrumbBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_breadcrumb('Home', reverse('myapp:home'))


class WildewidgetsView(
    MenuMixin,
    StandardWidgetMixin,
    TemplateView
):
    template_name: str = "academy_theme/base--wildewidgets.html"
    menu_class: Type[BasicMenu] = MainMenu
    menu_item: str = "Home"

    def get_content(self) -> WidgetListLayout:
        layout = WidgetListLayout("Wildewidgets Example")
        layout.add_widget(
            CardWidget(
                card_title='My Card',
                widget='Here is my card body',
            ),
            title='My Card',
            icon='info-square'
        )
        return layout

    def get_breadcrumbs(self) -> BreadcrumbBlock:
        breadcrumbs = BaseBreadcrumbs()
        breadcrumbs.add_breadcrumb('Wildewidgets')
        return breadcrumbs
```

If you do need to add Javascript or CSS, create your own `base--wildewidgets.html` that extends the `acadmey_theme`
one and and overrides its blocks as needed.  Example:

```html
{% extends 'academy_theme/base--wildewidgets.html' %}
{% load static %}

{% block extra_css %}
  <link rel="stylesheet" href="{% static 'myapp/css/styles.css' %}">
{% endblock %}

{% block extra_header_js %}
  <script src="{% static 'myapp/js/app.js %}" ></script>
{% endblock %}
```
