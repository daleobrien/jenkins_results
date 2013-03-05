
import requests
from django.shortcuts import HttpResponse
from django.conf import settings


def result(request, project):
    '''just get the json status for a build, and return an image ...'''

    data = requests.get(settings.JENKINS_URL.format(project=project),
                        auth=(settings.JENKINS_USER, settings.JENKINS_PASS))
    response = data.json()

    # figure out which icon
    icon = "failing.png"
    if "SUCCESS" == response['result']:
        icon = "passing.png"

    icon = __file__.replace("views.py", icon)

    image_data = open(icon, "rb").read()
    return HttpResponse(image_data, mimetype="image/png")
#
