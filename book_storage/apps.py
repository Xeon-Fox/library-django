from django.apps import AppConfig


class BookStorageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "book_storage"

    def ready(self):
        import book_storage.signals  # Импорт сигналов
