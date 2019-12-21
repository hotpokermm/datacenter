from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits =[]
    in_storage = Visit.objects.filter(leaved_at = None)

    for vis in in_storage:
        vis_info = {
            'who_entered': vis.passcard,
            'entered_at': vis.entered_at,
            'duration': format_duration(get_duration(vis)),
        }
        non_closed_visits.append(vis_info)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
