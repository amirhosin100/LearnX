from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Learn,FilmScores

@receiver(pre_save, sender=Learn)
def calculate_price(instance, sender, **kwargs):
    instance.discount_price = instance.price - (instance.price * instance.precent_off/100)
    instance.save()
