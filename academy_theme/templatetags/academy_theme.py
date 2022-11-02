from typing import Dict, Optional, Union, List, Any

from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('academy_theme/templatetags/breadcrumb.html')
def breadcrumb(title: str, *args, **kwargs) -> Dict[str, Union[str, Optional[str]]]:
    """
    Returns bootstrap compatible breadrumb.
    """
    url_name: str = 'NO NAME'
    if args:
        url_name = args[0]
        if len(args) == 1:
            url_args: List[Any] = []
        else:
            url_args = list(args[1:])
    return {
        'title': title,
        'url': reverse(url_name, *url_args, **kwargs) if url_name else None
    }
