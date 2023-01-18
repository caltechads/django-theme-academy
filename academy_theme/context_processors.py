from typing import Dict, Any
from django.conf import settings
from django.http.request import HttpRequest
from django.templatetags.static import static


def theme(request: HttpRequest) -> Dict[str, Any]:
    """
    Inject our theme variables into our templates.
    """
    theme_settings: Dict[str, Any] = getattr(settings, 'ACADEMY_THEME_SETTINGS', {})
    return {
        # Header
        'APPLE_TOUCH_ICON': static(theme_settings.get('APPLE_TOUCH_ICON', 'academy_theme/images/apple-touch-icon.png')),
        'FAVICON_32': static(theme_settings.get('FAVICON_32', 'academy_theme/images/favicon-32x32.png')),
        'FAVICON_16': static(theme_settings.get('FAVICON_16', 'academy_theme/images/favicon-16x16.png')),
        'FAVICON': static(theme_settings.get('FAVICON', 'academy_theme/images/favicon.ico')),
        'SITE_WEBMANIFEST': static(theme_settings.get('ORGANIZATION_NAME', 'academy_theme/images/site.webmanifest')),

        # Footer
        'ORGANIZATION_LINK': theme_settings.get('ORGANIZATION_LINK', 'https://google.com'),
        'ORGANIZATION_NAME': theme_settings.get('ORGANIZATION_NAME', 'Organization Name'),
        'ORGANIZATION_ADDRESS': theme_settings.get('ORGANIZATION_ADDRESS', 'Organization Address'),
        'COPYRIGHT_ORGANIZATION': theme_settings.get('COPYRIGHT_ORGANIZATION', 'Copyright Organization'),
        'FOOTER_LINKS': theme_settings.get('FOOTER_LINKS', []),

        # Settings
        'BODY_STYLE': theme_settings.get('BODY_STYLE', 'centered')
    }
