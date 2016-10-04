from django.shortcuts import render_to_response
from django.template import RequestContext
import pdb


def flumojiSplash(request):
    return render_to_response("visualization/flumoji_splash.html", {
    }, context_instance=RequestContext(request))

