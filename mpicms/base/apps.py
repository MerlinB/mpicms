from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    name = "mpicms.base"
    verbose_name = "Base"

    def ready(self):
        import mpicms.base.signals
