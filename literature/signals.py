from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=IdeaUtilization)
def create_story_raw(sender, instance, created, **kwargs):
    if created:
        StoryRaw.objects.create(idea=instance)
    else:
        instance.storyraw.save()
        



##########DO NOT ACTIVE BELOW SIGNAL############
# @receiver(post_save, sender=StoryOutline)
# def create_or_update_story(sender, instance, created, **kwargs):   
#     try:
#         story = instance.story  # Attempt to access the related Story
#     except Story.DoesNotExist:
#         story = None

#     if created or story is None:
#         # Create a new Story or update the existing one
#         story, created = Story.objects.get_or_create(story_outline=instance)
    
#     # Now, make sure that the instance.story is set properly
#     if instance.pk != story.pk:
#         instance.story = story
#         instance.save()