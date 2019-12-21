from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = Passcard.objects.filter(passcode = passcode)[0]
    visits = Visit.objects.filter(passcard = passcard)
    for vis in visits:
        vis_info = {
          "entered_at": vis.entered_at,
          "duration": format_duration(get_duration(vis)),
          "is_strange": str(is_visit_long(get_duration(vis))),
        }
        this_passcard_visits.append(vis_info)
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
