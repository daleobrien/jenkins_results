
import requests
from django.shortcuts import HttpResponse
from django.conf import settings
from django.views.decorators.cache import never_cache


@never_cache
def result(request, project):
    '''just get the json status for a build, and return an image ...'''

    data = requests.get(settings.JENKINS_URL.format(project=project),
                        auth=(settings.JENKINS_USER, settings.JENKINS_PASS))
    response = data.json()
    #for k, v in response.items():
        #print k, "\r\t\t\t", v

    # figure out which icon
    icon = "failing.png"
    if "SUCCESS" == response['result']:
        icon = "passing.png"

    if response['building']:
        icon = "unknown.png"

    icon = __file__.replace("views.py", icon)
    icon = icon.replace('.pngc', '.png')
        

    image_data = open(icon, "rb").read()
    r = HttpResponse(image_data, mimetype="image/png")
    r['Cache-Control'] = 'no-cache'
    return r
#
