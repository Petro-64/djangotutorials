from django.dispatch import Signal

new_category = Signal(providing_args=["subject"])