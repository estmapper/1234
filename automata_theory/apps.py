from django.apps import AppConfig


class AutomataTheoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "automata_theory"

    def ready(self):
        import automata_theory.signals
