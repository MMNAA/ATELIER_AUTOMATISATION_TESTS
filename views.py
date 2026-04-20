from django.http import JsonResponse
import subprocess

def health(request):
    result = subprocess.run(
        ["pytest", "-q"],
        capture_output=True,
        text=True
    )

    return JsonResponse({
        "status": "OK" if result.returncode == 0 else "FAIL",
        "output": result.stdout
    })