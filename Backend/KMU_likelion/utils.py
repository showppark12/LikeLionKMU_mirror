import os
import uuid

from django.utils import timezone


def get_file_path(instance, filename):
    time_path = timezone.now().strftime('%Y/%m/%d') 
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(time_path, filename)
