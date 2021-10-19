from calendar import timegm
from datetime import datetime

from django.conf import settings
from django.utils.functional import lazy
from django.utils.timezone import is_naive, make_aware, utc
from django.utils.html import strip_tags
from django.template.loader import render_to_string


def make_utc(dt):
    if settings.USE_TZ and is_naive(dt):
        return make_aware(dt, timezone=utc)

    return dt


def aware_utcnow():
    return make_utc(datetime.utcnow())


def datetime_to_epoch(dt):
    return timegm(dt.utctimetuple())


def datetime_from_epoch(ts):
    return make_utc(datetime.utcfromtimestamp(ts))


def format_lazy(s, *args, **kwargs):
    return s.format(*args, **kwargs)


def get_string_and_html(file, values):
    intermedia_values = {
        "servername": settings.SERVERNAME,
        "serverUrl": settings.SERVERURL,
    }
    final_values = {**intermedia_values, **values}
    html_content = render_to_string(file, final_values)
    text_content = strip_tags(html_content)
    return html_content, text_content


format_lazy = lazy(format_lazy, str)
