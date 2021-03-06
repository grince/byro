import django.dispatch

member_view = django.dispatch.Signal()
"""
Receives the member as sender, and additionally the request
Must return a dict:

    {
        "label": _("Fancy Member View"),
        "url": "/member/123/foo/",
        "url_name": "plugins:myplugin:foo_view",
    }
Please use byro.office.views.members.MemberView as base class for these views.
"""
