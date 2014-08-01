"""
gargoyle.decorators
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

from functools import wraps
from gargoyle import gargoyle

from django.shortcuts import redirect
from django.http import Http404


def switch_is_active(key, redirect_to=None, gargoyle=gargoyle):
    def _switch_is_active(func):
        @wraps(func)
        def wrapped(request, *args, **kwargs):
            if not gargoyle.is_active(key, request):
                if not redirect_to:
                    raise Http404('Switch \'%s\' is not active' % key)
                else:
                    return redirect(redirect_to)
            return func(request, *args, **kwargs)
        return wrapped
    return _switch_is_active
