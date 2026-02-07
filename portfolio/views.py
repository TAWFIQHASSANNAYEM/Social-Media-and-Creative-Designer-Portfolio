from pathlib import Path
import subprocess
import os

from django.conf import settings
from django.http import FileResponse, HttpResponse


def spa(request):
    index_path = Path(settings.BASE_DIR) / "frontend" / "dist" / "index.html"
    if not index_path.exists():
        # Build the frontend automatically
        frontend_dir = Path(settings.BASE_DIR) / "frontend"
        os.chdir(frontend_dir)
        try:
            subprocess.run(["npm", "install"], check=True, capture_output=True)
            subprocess.run(["npm", "run", "build"], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            pass  # Continue even if build fails
        finally:
            os.chdir(settings.BASE_DIR)

    if index_path.exists():
        return FileResponse(open(index_path, "rb"), content_type="text/html")

    return HttpResponse(
        "<h1>React build not found</h1>"
        "<p>Run <code>npm install</code> and <code>npm run build</code> in <code>frontend/</code>.</p>",
        content_type="text/html",
    )
