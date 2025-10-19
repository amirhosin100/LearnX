import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class BlogStorage(FileSystemStorage):
    location = os.path.join(settings.MEDIA_ROOT, 'ckdeitor')
    base_url = settings.MEDIA_URL + 'ckdeitor/'