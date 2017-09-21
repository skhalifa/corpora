from django.dispatch import receiver
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from .models import Sentence, Recording, QualityControl
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


@receiver(models.signals.post_save, sender=Sentence)
@receiver(models.signals.post_save, sender=Recording)
def create_quality_control_instance_when_object_created(
        sender, instance, **kwargs):
    qc, created = QualityControl.objects.get_or_create(
            object_id=instance.pk,
            content_type=ContentType.objects.get_for_model(instance)
        )
    if created:
        print "Created QC object {0}".format(qc.pk)
    else:
        print "QC object {0} exists".format(qc.pk)


@receiver(models.signals.pre_save, sender=Sentence)
def clear_quality_control_instance_when_object_modified(
        sender, instance, **kwargs):

    if isinstance(instance, Sentence):
        try:
            old_sentence = Sentence.objects.get(pk=instance.pk)

            if not (old_sentence.text == instance.text and \
                    old_sentence.language == instance.language):
                qc, qc_created = QualityControl.objects.get_or_create(
                        object_id=instance.pk,
                        content_type=ContentType.objects.get_for_model(instance)
                        )
                if not qc_created:
                    print "Clearing quality control"
                    qc.clear()
                    qc.save()

        except ObjectDoesNotExist:
            pass


@receiver(models.signals.pre_save, sender=Sentence)
@receiver(models.signals.pre_save, sender=Recording)
@receiver(models.signals.pre_save, sender=QualityControl)
def update_update_field_when_model_saved(sender, instance, **kwargs):
    instance.updated = timezone.now()


@receiver(models.signals.pre_save, sender=Sentence)
def split_sentence_when_period_in_sentence(sender, instance, **kwargs):
    parts = instance.text.split('.')
    for i in range(1, len(parts)):
        if len(parts[i]) < 6:  # This is arbitrary
            continue
        else:
            instance.text = parts[0]+'.'
            new_sentence = Sentence.objects.create(
                text=parts[i]+'.',
                language=instance.language)
            print "Created {0}".format(new_sentence)
