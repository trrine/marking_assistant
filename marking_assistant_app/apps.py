import os
from django.apps import AppConfig

from marking_assistant_project import settings


class MarkingAssistantAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "marking_assistant_app"

    def ready(self):
        filename = "marking_results.xlsx"
        excel_file_path = os.path.join(settings.MEDIA_ROOT, filename)

        if os.path.exists(excel_file_path):
            os.remove(excel_file_path)
