import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def run_audit(request):
    if request.method == "POST":
        os_version = request.POST.get('os_version')
        
        # Run the PowerShell script
        result = subprocess.run(["powershell", "S:\\Auditing-Tool-Dev\\Automatic-Auditing-BackEnd\\tool_dev\\CIS.ps1", os_version],
                                capture_output=True, text=True)
        
        if result.returncode == 0:
            return JsonResponse({"status": "success", "result": result.stdout.strip()})
        else:
            return JsonResponse({"status": "error", "result": result.stderr.strip()}, status=500)
