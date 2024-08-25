import subprocess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def run_audit(request):
    if request.method == 'POST':
        os_version = request.POST.get('os_version')

        script_map = {
            'Windows 10': "S:\Auditing-Tool-Dev\Automatic-Auditing-BackEnd\FireWall.ps1",
            'Windows 11': "S:\Auditing-Tool-Dev\Automatic-Auditing-BackEnd\FireWall.ps1",
            'Ubuntu 20.04': "/path/to/your/script_ubuntu2004.sh",
            'Ubuntu 22.04': "/path/to/your/script_ubuntu2204.sh",
            'Red Hat Enterprise Linux 8': "/path/to/your/script_rhel8.sh",
            'Red Hat Enterprise Linux 9': "/path/to/your/script_rhel9.sh",
        }

        script_path = script_map.get(os_version)

        if script_path:
            result = subprocess.run(["powershell", "-File", script_path], capture_output=True, text=True)
            return HttpResponse(result.stdout)
        else:
            return HttpResponse("Invalid OS version selected.", status=400)
    else:
        return HttpResponse("Invalid request method.", status=405)
