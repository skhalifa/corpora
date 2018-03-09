# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext as _

from django.template.context import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.conf import settings

from people.helpers import get_unknown_languages
from people.models import Group

from corpus import views

from django.contrib.sites.shortcuts import get_current_site


def home(request):
    if request.user.is_authenticated():
        return redirect('people:profile')
    else:
        groups = Group.objects.all().order_by('name')
        site = get_current_site(request)
        context = {
            'request': request,
            'groups': groups,
            'languages': get_unknown_languages(None),
            'x_title': site.name,
            'x_description': _("Teaching computers indigenous languages."),
        }

        return render(request, 'corpora/home.html', context)
        # return redirect('account/login')


def privacy(request):
    site = get_current_site(request)
    context = {
        'request': request,
        'languages': get_unknown_languages(None),
        'site': site,
        'x_title': _('Privacy Policy'),
        'x_description': _("Privacy policy for this website."),
    }

    return render(request, 'corpora/privacy.html', context)


def rules(request):
    site = get_current_site(request)
    context = {
        'request': request,
        'languages': get_unknown_languages(None),
        'site': site,
        'x_title': _('Rules'),
        'x_description': _("Rules for our competitions."),
    }

    return render(request, 'corpora/rules.html', context)
