from pathlib import Path

from django.conf import settings
from django.http import FileResponse, HttpResponse


def spa(request):
    index_path = Path(settings.BASE_DIR) / "frontend" / "dist" / "index.html"
    if index_path.exists():
        return FileResponse(open(index_path, "rb"), content_type="text/html")

    return HttpResponse(
        "<h1>React build not found</h1>"
        "<p>Run <code>npm install</code> and <code>npm run build</code> in <code>frontend/</code>.</p>",
        content_type="text/html",
    )
