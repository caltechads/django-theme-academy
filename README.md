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
