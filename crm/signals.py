

@receiver(post_save)
def search_on_post_save(sender, instance, **kwargs):
    if issubclass(sender, Employee):
        EmailToken.objects.create(user=instance)